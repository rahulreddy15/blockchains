import asyncio
import time

async def greet(name, delay):
    await asyncio.sleep(delay)
    print("{0}: I waited {1} seconds before saying hello!".format(name, delay))

async def main():
    task1 = asyncio.create_task(greet('t1', 3))
    task2 = asyncio.create_task(greet('t2', 2))
    task3 = asyncio.create_task(greet('t3', 2))

    start_time = time.time()
    print("0.00 s -> Program Start")
    await task1
    await task2
    await task3

    print('{0} s -> Program End'.format(time.time()-start_time))

asyncio.run(main())
