import time

start_time = time.time()

a = 10000000
b = 25000000

while a <= b:
    print(a)
    a += 1

print("Execution time: %s seconds" % (time.time() - start_time))
