import aiomysql
import asyncio


class MySQLConnectionPool:
    def __init__(self, host, port, user, password, db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.pool = None

    async def __aenter__(self):
        await self.init()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.destroy()

    async def init(self):
        self.pool = await aiomysql.create_pool(host=self.host, port=self.port,
                                               user=self.user, password=self.password, db=self.db)

    async def destroy(self):
        self.pool.close()
        await self.pool.wait_closed()

    async def query(self, sql, arg=None, is_dict=True):
        cur_type = aiomysql.Cursor
        if is_dict:
            cur_type = aiomysql.DictCursor
        async with self.pool.acquire() as conn:
            async with conn.cursor(cur_type) as cur:
                await cur.execute(sql, arg)
                result = await cur.fetchall()
                return result

    async def query_once(self, sql, arg=None, is_dict=True):
        cur_type = aiomysql.SSCursor
        if is_dict:
            cur_type = aiomysql.SSDictCursor
        async with self.pool.acquire() as conn:
            async with conn.cursor(cur_type) as cur:
                await cur.execute(sql, arg)
                row = await cur.fetchone()
                while row:
                    yield row
                    row = await cur.fetchone()

    async def execute(self, sql, arg=None):
        async with self.pool.get() as conn:
            async with conn.cursor() as cur:
                if isinstance(arg, list):
                    affect_row = await cur.executemany(sql, arg)
                else:
                    affect_row = await cur.execute(sql, arg)
                await conn.commit()
                return affect_row


async def go():
    async with MySQLConnectionPool(host="192.168.1.214", port=3306, user='root', password='0hOpPCWhvLfX00xe', db='wb_test_log') as pool:
        result = await pool.query("select * from ypds_log_model_1 where id = %s", 1)
        print(result)
        # async for x in pool.query_iter("select * from ypds_log_model_1"):
        #     print(x)

if "__main__" == __name__:
    asyncio.run(go())
