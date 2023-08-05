# from symbol import testlist_statest_tabler_expr
import numpy as np

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
    
    return int(DP_table[0, array_length-1])

timber_array = [33, 28, 35, 25,29,34,28,32]
timber_array = np.asarray(timber_array)

result = timberDPAlgo(timber_array)

print('Timber: ', timber_array)
print('Maximum sum length is :', result)