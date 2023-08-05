import numpy as np
import random
import time

def timberDPAlgo(timber_array):
    array_length = len(timber_array)
    DP_table = np.ones((array_length, array_length))

    for i in range(array_length):
        DP_table[i, i] = timber_array[i]
    
    for i in range(array_length-1):
        DP_table[i, i+1] = max(timber_array[i], timber_array[i+1])

    for k in range(2, array_length):
        for i in range(array_length-k):
            j = i + k
            DP_table[i, j] = max((timber_array[i]+min(DP_table[i+2, j], DP_table[i+1, j-1])), (timber_array[j]+min(DP_table[i+1, j-1], DP_table[i, j-2])))
    
    return int(DP_table[0, -1])

# 1: n = 100
n = 100
timber_array = random.sample(range(1, 101), n)
start_time = time.process_time()
result = timberDPAlgo(timber_array)
end_time = time.process_time()

print('List: ', timber_array)
print('Result when n is ' + str(n) + ': ', result)
print('Execution time: ', end_time-start_time, 'seconds')
print()

# 2: n = 500
n = 500
timber_array = random.sample(range(1, 501), n)
start_time = time.process_time()
result = timberDPAlgo(timber_array)
end_time = time.process_time()

print('List: ', timber_array)
print('Result when n is ' + str(n) + ': ', result)
print('Execution time: ', end_time-start_time, 'seconds')
print()

# 3: n = 1000
n = 1000
timber_array = random.sample(range(1, 1001), n)
start_time = time.process_time()
result = timberDPAlgo(timber_array)
end_time = time.process_time()

print('List: ', timber_array)
print('Result when n is ' + str(n) + ': ', result)
print('Execution time: ', end_time-start_time, 'seconds')
print()

# 4: n = 2000
n = 2000
timber_array = random.sample(range(1, 2001), n)
start_time = time.process_time()
result = timberDPAlgo(timber_array)
end_time = time.process_time()

print('List: ', timber_array)
print('Result when n is ' + str(n) + ': ', result)
print('Execution time: ', end_time-start_time, 'seconds')
print()

# 5: n = 3000
n = 3000
timber_array = random.sample(range(1, 3001), n)
start_time = time.process_time()
result = timberDPAlgo(timber_array)
end_time = time.process_time()

print('List: ', timber_array)
print('Result when n is ' + str(n) + ': ', result)
print('Execution time: ', end_time-start_time, 'seconds')
print()

# 6: n = 4000
n = 4000
timber_array = random.sample(range(1, 4001), n)
start_time = time.process_time()
result = timberDPAlgo(timber_array)
end_time = time.process_time()

print('List: ', timber_array)
print('Result when n is ' + str(n) + ': ', result)
print('Execution time: ', end_time-start_time, 'seconds')
print()

# 7: n = 5000
n = 5000
timber_array = random.sample(range(1, 5001), n)
start_time = time.process_time()
result = timberDPAlgo(timber_array)
end_time = time.process_time()

print('List: ', timber_array)
print('Result when n is ' + str(n) + ': ', result)
print('Execution time: ', end_time-start_time, 'seconds')
print()

# 8: n=6000
n = 6000
timber_array = random.sample(range(1, 6001), n)
start_time = time.process_time()
result = timberDPAlgo(timber_array)
end_time = time.process_time()

print('List: ', timber_array)
print('Result when n is ' + str(n) + ': ', result)
print('Execution time: ', end_time-start_time, 'seconds')
print()

# # 9: n=7000
# n = 7000
# timber_array = random.sample(range(1, 7001), n)
# start_time = time.process_time()
# result = timberDPAlgo(timber_array)
# end_time = time.process_time()

# print('List: ', timber_array)
# print('Result when n is ' + str(n) + ': ', result)
# print('Execution time: ', end_time-start_time, 'seconds')
# print()

# # 10: n=8000
# n = 8000
# timber_array = random.sample(range(1, 8001), n)
# start_time = time.process_time()
# result = timberDPAlgo(timber_array)
# end_time = time.process_time()

# print('List: ', timber_array)
# print('Result when n is ' + str(n) + ': ', result)
# print('Execution time: ', end_time-start_time, 'seconds')
# print()

# #11: n=9000
# n = 9000
# timber_array = random.sample(range(1, 9001), n)
# start_time = time.process_time()
# result = timberDPAlgo(timber_array)
# end_time = time.process_time()

# print('List: ', timber_array)
# print('Result when n is ' + str(n) + ': ', result)
# print('Execution time: ', end_time-start_time, 'seconds')
# print()

# # 12: n=10000
# n = 10000
# timber_array = random.sample(range(1, 10001), n)
# start_time = time.process_time()
# result = timberDPAlgo(timber_array)
# end_time = time.process_time()

# print('List: ', timber_array)
# print('Result when n is ' + str(n) + ': ', result)
# print('Execution time: ', end_time-start_time, 'seconds')
# print()
