import aiohttp
import crawler.common as cc


async def main():
    async with aiohttp.ClientSession() as session:
        html = await get("https://www.qq.com", session)
        return await process(html, session)


async def get(url, session):
    async with session.get(url, headers=cc.default_headers) as resp:
        encoding = cc.get_coding(resp)
        return await resp.text(encoding=encoding)


async def process(html, session):
    print(html)
