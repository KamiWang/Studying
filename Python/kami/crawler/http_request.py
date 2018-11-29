import aiohttp
import asyncio

default_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/70.0.3538.102 Safari/537.36",
    "Accept-Language": "zh-CN,zh;q=0.9", "Accept-Encoding": "gzip, deflate, br", "Connection": "keep-alive"}


class HTTPRequestClient:
    def __init__(self):
        self.session = None
        self.headers = default_headers

    async def __aenter__(self):
        await self.init()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.destory()

    async def init(self):
        self.session = aiohttp.ClientSession()

    async def destory(self):
        await self.session.close()

    async def get(self, url):
        async with self.session.get(url, headers=self.headers) as response:
            return await response.text(self.get_coding(response))

    def get_coding(self, response):
        charset = "utf-8"
        try:
            charset = response.get_encoding()
        except Exception:
            return charset
        if charset.find("gb") >= 0:
            charset = "gb18030"
        return charset


async def go():
    async with HTTPRequestClient() as client:
        html = await client.get("https://www.qq.com")
        print(html)


if __name__ == "__main__":
    asyncio.run(go())
