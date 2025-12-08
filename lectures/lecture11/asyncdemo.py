import asyncio

async def hello(i, n):
    print(f"hello {i} started, going to sleep for {n} seconds")
    await asyncio.sleep(n)
    print(f"hello {i} done")

async def main():
    task1 = asyncio.create_task(hello(1, 4))  
    task2 = asyncio.create_task(hello(2, 6))
    await task1
    await task2

asyncio.run(main())

