# import asyncio

# async def cor1():
#     print("cor1 start")
#     for i in range(10):
#         await asyncio.sleep(1.5)
#         print("cor1", i)

# async def cor2():
#     print("cor2 start")
#     for i in range(15):
#         await asyncio.sleep(1)
#         print("cor2", i)

# async def main():
#     await asyncio.gather(cor1(), cor2())

# asyncio.run(main())

import threading
import time

# def task(name):
#     print(f"Task {name} starting...")
#     time.sleep(2)
#     print(f"Task {name} finished!")


# t1 = threading.Thread(target=task, args=("A",))
# t2 = threading.Thread(target=task, args=("B",))

# t1.start()
# t2.start()

# t1.join()
# t2.join()




import asyncio
import aiohttp

URL = "https://jsonplaceholder.typicode.com/todos/1"

async def fetch(session, i):
    async with session.get(URL) as response:
        data = await response.json()
        print(f"Request {i}:", data)

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []

        for i in range(10):  # 10 parallel requests
            tasks.append(fetch(session, i))

        await asyncio.gather(*tasks)

asyncio.run(main())