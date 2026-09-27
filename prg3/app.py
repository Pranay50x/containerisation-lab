import time 
print("starting task ...")

start = time.time() 

while ((time.time() -start) < 30): 
    x = 0 
    for i in range(100000): 
        x += i*i 
print("Task done")

