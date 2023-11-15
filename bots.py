import threading
import time
import json

with open('inventory.dat', 'r') as f:
    inventory = json.load(f)


def bot_clerk(lst):
    cart = []
    threadLock = threading.Lock()

    robots = [[], [], []]

    for i, item in enumerate(lst):
        robots[i % 3].append(item)

    threads = []
    for robot in robots:
        thread = threading.Thread(target=robot_fetcher, args=(robot, cart, threadLock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    
    return cart

def robot_fetcher(nums, cart, lock):
    for number in nums:
        item, wait = inventory[number]
        time.sleep(wait)
        with lock:
            cart.append([number, item])

