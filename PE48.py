import time
start_time = time.time()

sum = 0
for i in range(1001):
    sum = sum + i**i

print(sum - 1)
print("--- %s seconds ---" % (time.time() - start_time))
