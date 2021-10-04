import sys
import random
import time
import os
import signal

def handler2(sig, frame):
    os.system('rm data/Structured_Streaming/data_*')
    sys.exit()

def basic_operations():
    signal.signal(signal.SIGINT, handler2)
    idx = 1
    while True:
        with open(f"data/Structured_Streaming/data_"+str(idx).zfill(4)+".csv", "w") as f:
            for i in range(50):
                qty = str(random.randint(1,10))
                price = str(round(random.uniform(1.0, 21.0), 2))
                buy = "buy" if random.randint(1,10) <= 8 else "sell"
                f.write("-,1,1," + ",".join((qty, price, buy)) + "\n")
        time.sleep(5)
        idx += 1
    signal.pause()


length3 = 1
def handler3(sig, frame):
    global length3
    for idx in range(1, length3+1):
        os.system(f"mv data/Structured_Streaming/twitter_{str(idx).zfill(2)} data/Structured_Streaming/Twitter/twitter_{str(idx).zfill(2)}")
    sys.exit()

def window():
    global length3
    signal.signal(signal.SIGINT, handler3)
    for idx in range(1, 31):
        os.system(f"mv data/Structured_Streaming/Twitter/twitter_{str(idx).zfill(2)} data/Structured_Streaming/twitter_{str(idx).zfill(2)}")
        length3 = idx
        time.sleep(5)
    signal.pause()


if not len(sys.argv) > 1:
    print("not enough arguments, usecase: 'python3 generator.py [NUM]'")
    sys.exit()
if int(sys.argv[1]) == 2:
    basic_operations()
elif int(sys.argv[1]) == 3:
    window()
