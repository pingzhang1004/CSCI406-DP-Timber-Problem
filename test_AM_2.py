import numpy as np
import random
import time

def timberRecursiveAlgo(i, j, timber_array):
    global callCount
    callCount= callCount+1
    if j == i:
        return timber_array[i-1]
    elif j == i+1:
        return max(timber_array[i-1], timber_array[j-1])
    else:
        return(max((timber_array[i-1]+min(timberRecursiveAlgo(i+2, j, timber_array), timberRecursiveAlgo(i+1, j-1, timber_array))), (timber_array[j-1]+min(timberRecursiveAlgo(i+1, j-1, timber_array), timberRecursiveAlgo(i, j-2, timber_array)))))

# 0: n=1
n = 1
timber_array = random.sample(range(1, 50), n)
callCount = 0
start_time = time.process_time()
result = timberRecursiveAlgo(1, len(timber_array), timber_array)
end_time = time.process_time()

print('List: ', timber_array)
print('Result when n is ' + str(n) + ': ', result)
print('Call the T(i,j) counts is : ', callCount)
print('Execution time: ', end_time-start_time, 'seconds')
print()

# 1: n=2
n = 2
timber_array = random.sample(range(1, 50), n)
callCount = 0
start_time = time.process_time()
result = timberRecursiveAlgo(1, len(timber_array), timber_array)
end_time = time.process_time()

print('List: ', timber_array)
print('Result when n is ' + str(n) + ': ', result)
print('Call the T(i,j) counts is : ', callCount)
print('Execution time: ', end_time-start_time, 'seconds')
print()

# 2: n=3
n = 3
timber_array = random.sample(range(1, 50), n)
callCount = 0
start_time = time.process_time()
result = timberRecursiveAlgo(1, len(timber_array), timber_array)
end_time = time.process_time()

print('List: ', timber_array)
print('Result when n is ' + str(n) + ': ', result)
print('Call the T(i,j) counts is : ', callCount)
print('Execution time: ', end_time-start_time, 'seconds')
print()

# 3: n=4
n = 4
timber_array = random.sample(range(1, 50), n)
callCount = 0
start_time = time.process_time()
result = timberRecursiveAlgo(1, len(timber_array), timber_array)
end_time = time.process_time()

print('List: ', timber_array)
print('Result when n is ' + str(n) + ': ', result)
print('Call the T(i,j) counts is : ', callCount)
print('Execution time: ', end_time-start_time, 'seconds')
print()

# 4: n=5
n = 5
timber_array = random.sample(range(1, 50), n)
callCount = 0
start_time = time.process_time()
result = timberRecursiveAlgo(1, len(timber_array), timber_array)
end_time = time.process_time()

print('List: ', timber_array)
print('Result when n is ' + str(n) + ': ', result)
print('Call the T(i,j) counts is : ', callCount)
print('Execution time: ', end_time-start_time, 'seconds')
print()

# 5: n=6
n = 6
timber_array = random.sample(range(1, 50), n)
callCount = 0
start_time = time.process_time()
result = timberRecursiveAlgo(1, len(timber_array), timber_array)
end_time = time.process_time()

print('List: ', timber_array)
print('Result when n is ' + str(n) + ': ', result)
print('Call the T(i,j) counts is : ', callCount)
print('Execution time: ', end_time-start_time, 'seconds')
print()

# 6: n=7
n = 7
timber_array = random.sample(range(1, 50), n)
callCount = 0
start_time = time.process_time()
result = timberRecursiveAlgo(1, len(timber_array), timber_array)
end_time = time.process_time()

print('List: ', timber_array)
print('Result when n is ' + str(n) + ': ', result)
print('Call the T(i,j) counts is : ', callCount)
print('Execution time: ', end_time-start_time, 'seconds')
print()

# 7: n=8
n = 8
timber_array = random.sample(range(1, 50), n)
callCount = 0
start_time = time.process_time()
result = timberRecursiveAlgo(1, len(timber_array), timber_array)
end_time = time.process_time()

print('List: ', timber_array)
print('Result when n is ' + str(n) + ': ', result)
print('Call the T(i,j) counts is : ', callCount)
print('Execution time: ', end_time-start_time, 'seconds')
print()

# 8: n=9
n = 9
timber_array = random.sample(range(1, 50), n)
callCount = 0
start_time = time.process_time()
result = timberRecursiveAlgo(1, len(timber_array), timber_array)
end_time = time.process_time()

print('List: ', timber_array)
print('Result when n is ' + str(n) + ': ', result)
print('Call the T(i,j) counts is : ', callCount)
print('Execution time: ', end_time-start_time, 'seconds')
print()

# 9: n=10
n = 10
timber_array = random.sample(range(1, 50), n)
callCount = 0
start_time = time.process_time()
result = timberRecursiveAlgo(1, len(timber_array), timber_array)
end_time = time.process_time()

print('List: ', timber_array)
print('Result when n is ' + str(n) + ': ', result)
print('Call the T(i,j) counts is : ', callCount)
print('Execution time: ', end_time-start_time, 'seconds')
print()

# 10: n=11
n = 11
timber_array = random.sample(range(1, 50), n)
callCount = 0
start_time = time.process_time()
result = timberRecursiveAlgo(1, len(timber_array), timber_array)
end_time = time.process_time()

print('List: ', timber_array)
print('Result when n is ' + str(n) + ': ', result)
print('Call the T(i,j) counts is : ', callCount)
print('Execution time: ', end_time-start_time, 'seconds')
print()

#11: n=12
n = 12
timber_array = random.sample(range(1, 50), n)
callCount = 0
start_time = time.process_time()
result = timberRecursiveAlgo(1, len(timber_array), timber_array)
end_time = time.process_time()

print('List: ', timber_array)
print('Result when n is ' + str(n) + ': ', result)
print('Call the T(i,j) counts is : ', callCount)
print('Execution time: ', end_time-start_time, 'seconds')
print()

# 12: n=13
n = 13
timber_array = random.sample(range(1, 50), n)
callCount = 0
start_time = time.process_time()
result = timberRecursiveAlgo(1, len(timber_array), timber_array)
end_time = time.process_time()

print('List: ', timber_array)
print('Result when n is ' + str(n) + ': ', result)
print('Call the T(i,j) counts is : ', callCount)
print('Execution time: ', end_time-start_time, 'seconds')
print()

# 13: n=14
n = 14
timber_array = random.sample(range(1, 50), n)
callCount = 0
start_time = time.process_time()
result = timberRecursiveAlgo(1, len(timber_array), timber_array)
end_time = time.process_time()

print('List: ', timber_array)
print('Result when n is ' + str(n) + ': ', result)
print('Call the T(i,j) counts is : ', callCount)
print('Execution time: ', end_time-start_time, 'seconds')
print()




