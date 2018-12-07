import string
import aiomysql
from archive.archive_base import SQLMaker, EngineBase


class MySQLMaker(SQLMaker):
    delete_sql = string.Template("delete from ${table} where ${condition}")
    select_sql = string.Template("select ${fields} from ${table} where ${condition} ${order} ${limit}")
    update_sql = string.Template("update ${table} set ${assign} where ${condition}")
    insert_sql = string.Template("insert into ${table} (${fields}) values(${values})")
    count_sql = string.Template("select count(*) from ${table} where ${condition}")

    def __init__(self):
        self.matching = dict()
        self.template = None
        self.arguments = list()

    def table(self, name: str) -> SQLMaker:
        self.matching["table"] = name
        return self

    def select(self, fields: list = None) -> SQLMaker:
        self.template = MySQLMaker.select_sql
        if not fields:
            fields_str = "*"
        else:
            fields_str = ",".join(fields)
        self.matching["fields"] = fields_str
        self.matching["condition"] = "true"
        self.matching["order"] = ""
        self.matching["limit"] = ""
        return self

    def insert(self, key_values: dict) -> SQLMaker:
        self.template = MySQLMaker.insert_sql
        fields_list = list()
        values_list = list()
        values_arg_list = list()
        for key in key_values:
            fields_list.append(key)
            if isinstance(key_values[key], str):
                values_list.append("%s")
                values_arg_list.append(key_values[key])
            else:
                values_list.append(str(key_values[key]))
        self.matching["fields"] = ",".join(fields_list)
        self.matching["values"] = ",".join(values_list)
        self.arguments[0:0] = values_arg_list
        return self

    def update(self, key_values: dict) -> SQLMaker:
        self.template = MySQLMaker.update_sql
        assign_str_list = list()
        assign_args_list = list()
        for key in key_values:
            if isinstance(key_values[key], str):
                assign_str_list.append(key + "=%s")
                assign_args_list.append(key_values[key])
            else:
                assign_str_list.append(key + "=" + str(key_values[key]))
        self.matching["assign"] = ','.join(assign_str_list)
        self.arguments[0:0] = assign_args_list
        return self

    def delete(self) -> SQLMaker:
        self.template = MySQLMaker.delete_sql
        return self

    def count(self) -> SQLMaker:
        self.template = MySQLMaker.count_sql
        self.matching["condition"] = "true"
        return self

    def condition(self, cond: str, arguments: list) -> SQLMaker:
        self.matching["condition"] = cond
        self.arguments.extend(arguments)
        return self

    def order_by(self, fields: list, reverse: bool) -> SQLMaker:
        if not fields:
            return
        order_str = "order by " + ",".join(fields)
        if reverse:
            order_str += " desc"
        else:
            order_str += " asc"
        self.matching["order"] = order_str
        return self

    def limit(self, count: int, offset: int = 0) -> SQLMaker:
        if not count:
            return
        self.matching["limit"] = "limit %d,%d" % (offset, count)
        return self

    def make(self):
        sql = self.template.substitute(self.matching)
        if not self.arguments:
            return sql, None

        new_args = list()
        for i in range(len(self.arguments)):
            if isinstance(self.arguments[i], str):
                new_args.append(self.arguments[i])
                self.arguments[i] = "%s"
        return sql % tuple(self.arguments), tuple(new_args) if new_args else None


class MySQLEngine(EngineBase):
    def __init__(self, host, port, user, password, schema):
        self.host = host
        self.port = int(port)
        self.user = user
        self.password = password
        self.schema = schema
        self.pool = None

    async def __aenter__(self):
        await self.initialize()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.destroy()

    async def initialize(self):
        self.pool = await aiomysql.create_pool(echo=True, host=self.host, port=self.port, user=self.user,
                                               password=self.password, db=self.schema)

    async def destroy(self):
        self.pool.close()
        await self.pool.wait_closed()

    def sql_maker(self) -> MySQLMaker:
        return MySQLMaker()

    async def query(self, sql_maker) -> dict:
        sql, args = sql_maker.make()
        return await self.raw_query(sql, args, dict)

    async def query_once(self, sql_maker):
        sql, args = sql_maker.make()
        async for it in self.raw_query_once(sql, args, dict):
            yield it

    async def execute(self, sql_maker) -> int:
        sql, args = sql_maker.make()
        return await self.raw_execute(sql, args)

    async def raw_query(self, sql, arg=None, result_type=tuple):
        cursor_type = aiomysql.Cursor
        if result_type is dict:
            cursor_type = aiomysql.DictCursor
        async with self.pool.acquire() as conn:
            async with conn.cursor(cursor_type) as cur:
                await cur.execute(sql, arg)
                return await cur.fetchall()

    async def raw_query_once(self, sql, arg=None, result_type=tuple):
        cursor_type = aiomysql.SSCursor
        if result_type is dict:
            cursor_type = aiomysql.SSDictCursor
        async with self.pool.acquire() as conn:
            async with conn.cursor(cursor_type) as cur:
                await cur.execute(sql, arg)
                row = await cur.fetchone()
                while row:
                    yield row
                    row = await cur.fetchone()

    async def raw_execute(self, sql, arg=None):
        async with self.pool.acquire() as conn:
            async with conn.cursor() as cur:
                if isinstance(arg, list):
                    affect_row = await cur.executemany(sql, arg)
                else:
                    affect_row = await cur.execute(sql, arg)
                await conn.commit()
                return affect_row
