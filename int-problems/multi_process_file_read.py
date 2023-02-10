
import os 
import time
import multiprocessing

base_path = '/home/uptycs/shyam/dsa-practice-proj/dsa-and-int-prob/int-problems'
files = os.listdir(base_path)
files = [base_path+'/'+i for i in files]

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

pool = multiprocessing.Pool(processes=10)
output = pool.map(m1, files)

t2 = time.time()

print(t2-t1)