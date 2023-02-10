
import os 
import time
from concurrent import futures
from concurrent.futures.thread import ThreadPoolExecutor
from threading import Thread

base_path = '/home/uptycs/shyam/dsa-practice-proj/dsa-and-int-prob/int-problems'
files = os.listdir(base_path)

def  m1(file):
    if os.path.isdir(file):
        return

    with open(file) as f:
        while True:
            buff = f.read(1024)
            if buff:
                # print(buff)
                pass
            else:
                return
            
res = []

t1 = time.time()

with ThreadPoolExecutor(max_workers=10) as thread_pool_executor:
    
    fts = [thread_pool_executor.submit(m1, base_path+'/'+i) for i in files]
        
    for future in futures.as_completed(fts):
        res.append(future)
    

t2 = time.time()

print(t2-t1)


import time 
def m(n):
    print(n)
    time.sleep(3)


t1 = Thread(target=m, args=(5,))
t2 = Thread(target=m, args=(10,))
t1.start()
t2.start()
# t1.join()
# t2.join()