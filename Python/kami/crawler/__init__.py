import asyncio
import aiohttp

default_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
                   "Accept-Language": "zh-CN,zh;q=0.9", "Accept-Encoding": "gzip, deflate, br", "Connection": "keep-alive"}


class Crawler:
    def __init__(self):
        self.tasks = list()
        self.func_process = lambda html: print(html)
        global default_headers
        self.headers = default_headers

    def run(self, url_list):
        asyncio.run(self._do_run(url_list))

    def _get_coding(self, resp):
        charset = "utf-8"
        try:
            charset = resp.get_encoding()
        except Exception:
            return charset
        if charset.find("gb") >= 0:
            charset = "gb18030"
        return charset

    async def _do_run(self, url_list):
        for url in url_list:
            self.tasks.append(asyncio.create_task(self._get(url)))
        await asyncio.gather(*self.tasks)

    async def _get(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=self.headers) as resp:
                html = await resp.text(self._get_coding(resp))
                if self.func_process:
                    self.func_process(html)


if __name__ == "__main__":
    aa = Crawler()
    aa.run(["https://www.qq.com"])
