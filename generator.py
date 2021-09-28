import sys
import random
import time
import os
import signal

def handler(sig, frame):
    os.system('rm data/data_*')
    sys.exit()

signal.signal(signal.SIGINT, handler)
idx = 1
while True:
    with open(f"data/data_"+str(idx).zfill(4)+".csv", "w") as f:
        for i in range(50):
            qty = str(random.randint(1,10))
            price = str(round(random.uniform(1.0, 21.0), 2))
            buy = "buy" if random.randint(1,10) <= 8 else "sell"
            f.write("-,1,1," + ",".join((qty, price, buy)) + "\n")
    time.sleep(5)
    idx += 1

signal.pause()
