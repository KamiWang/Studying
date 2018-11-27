import aiohttp
import re


def get_coding(response):
    charset = "utf-8"
    if response.charset:
        charset = response.charset.lower()
        if charset.find("gb") >= 0:
            charset = "gbk"
    return charset


async def run_task(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            html = await response.text(get_coding(response))
            process_html(html)


def process_html(html):
    print(html)
