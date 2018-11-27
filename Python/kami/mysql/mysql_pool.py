import aiomysql
import asyncio


class MySQLConntionPool:
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
        await self.destory()

    async def init(self):
        self.pool = await aiomysql.create_pool(host=self.host, port=self.port, user=self.user, password=self.password, db=self.db)

    async def destory(self):
        self.pool.close()
        await self.pool.wait_closed()

    async def query(self, sql):
        async with self.pool.get() as conn:
            async with conn.cursor() as cur:
                await cur.execute(sql)
                result = await cur.fetchall()
                return result

    async def query_row(self, sql):
        async with self.pool.get() as conn:
            async with conn.cursor() as cur:
                await cur.execute(sql)
                row = await cur.fetchone()
                while row:
                    yield row
                    row = await cur.fetchone()

    async def excute(self, sql):
        async with self.pool.get() as conn:
            async with conn.cursor() as cur:
                affect_row = await cur.execute(sql)
                await conn.commit()
                return affect_row


async def go():
    async with MySQLConntionPool(host="192.168.1.214", port=3306, user='root', password='0hOpPCWhvLfX00xe', db='wb_test_log') as pool:
        result = await pool.query("select * from ypds_log_model_1")
        print(result)
        async for x in pool.query_row("select * from ypds_log_model_1"):
            print(x)

if "__main__" == __name__:
    asyncio.run(go())
