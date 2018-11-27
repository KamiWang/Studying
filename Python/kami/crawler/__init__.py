import asyncio

import crawler.http_task as cht


async def main(url_list):
    tasks = list()
    for url in url_list:
        tasks.append(asyncio.create_task(cht.run_task(url)))
    await asyncio.gather(*tasks)


def run(url_list):
    asyncio.run(main(url_list))
