import numpy as np

def timberRecursiveAlgo(i, j, timber_array):
    global callCount
    callCount= callCount+1
    if j == i:
        return timber_array[i-1]
    elif j == i+1:
        return max(timber_array[i-1], timber_array[j-1])
    else:
        return(max((timber_array[i-1]+min(timberRecursiveAlgo(i+2, j, timber_array), timberRecursiveAlgo(i+1, j-1, timber_array))), (timber_array[j-1]+min(timberRecursiveAlgo(i+1, j-1, timber_array), timberRecursiveAlgo(i, j-2, timber_array)))))


timber_array = [33, 28, 35, 25, 29, 34, 28, 32]
timber_array = np.asarray(timber_array)
callCount = 0
result = timberRecursiveAlgo(1, len(timber_array), timber_array)

print('Timber: ', timber_array)
print('Maximum sum length is :', result)
print('The number of Call the T(i,j) is : ', callCount)

