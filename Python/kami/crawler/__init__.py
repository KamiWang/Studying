import asyncio

import crawler.template as template


async def join_task():
    all_tasks = list()
    all_tasks.append(asyncio.create_task(template.main()))
    await asyncio.gather(*all_tasks)


def run():
    asyncio.run(join_task())
