import asyncio
import datetime
import random
import requests
import time


async def sleeping(seconds):
    loop = asyncio.get_event_loop()
    print(f'start:  wait for {seconds}s.')
    await loop.run_in_executor(None, time.sleep, seconds)
    print(f'finish: wait for {seconds}s.')


async def get_global_ip(seconds):
    loop = asyncio.get_event_loop()
    res = await loop.run_in_executor(None, requests.get, 'http://inet-ip.info/ip')
    await sleeping(seconds)
    return res


def main():
    before = datetime.datetime.now()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    timers = [1, 2, 3, 4, 5]
    random.shuffle(timers)

    gather = asyncio.gather(
        get_global_ip(timers[0]),
        get_global_ip(timers[1]),
        get_global_ip(timers[2]),
        get_global_ip(timers[3]),
        get_global_ip(timers[4]),
    )
    results = loop.run_until_complete(gather)
    print(results)

    after = datetime.datetime.now()
    print(f'{(after - before).seconds}s')


if __name__ == '__main__':
    main()
