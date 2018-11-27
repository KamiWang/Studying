import asyncio
import aiohttp
import crawler.template as template
import crawler.common as cc


def run():
    asyncio.run(join_task())


async def join_task():
    all_tasks = list()
    all_tasks.append(asyncio.create_task(template.main()))
    await asyncio.gather(*all_tasks)


async def get_web_content(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=cc.default_headers) as resp:
            return await resp.text(cc.get_coding(resp))
