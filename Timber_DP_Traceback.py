# from symbol import testlist_statest_tabler_expr
import numpy as np

def timberDPAlgoTraceback(timber_array):
    array_length = len(timber_array)
    DP_table = np.ones((array_length, array_length))
    Traceback_table = np.ones((array_length, array_length))
    left = -1 # left
    right = -2 # right

    for i in range(array_length):
        DP_table[i, i] = timber_array[i]
        Traceback_table[i, i] = timber_array[i]
    
    for i in range(array_length-1):
        DP_table[i, i+1] = max(timber_array[i], timber_array[i+1])
        if timber_array[i] >= timber_array[i+1]:
            Traceback_table[i, i+1] = -1    # left
        else:
            Traceback_table[i, i+1] = -2    # right

    for k in range(2, array_length):
        for i in range(array_length-k):
            j = i + k
            DP_table[i, j] = max((timber_array[i]+min(DP_table[i+2, j], DP_table[i+1, j-1])), (timber_array[j]+min(DP_table[i+1, j-1], DP_table[i, j-2])))

            if (timber_array[i]+min(DP_table[i+2, j], DP_table[i+1, j-1])) >= (timber_array[j]+min(DP_table[i+1, j-1], DP_table[i, j-2])):
                Traceback_table[i, j] = -1  # left
            else:
                Traceback_table[i, j] = -2  # right

    temp_i = 0
    temp_j = array_length - 1
    output_order = np.ones(array_length).astype(np.int)
    idx_output_order = 0
    while temp_i != temp_j:
        direction = Traceback_table[temp_i, temp_j]
        if direction == -1: # left
            output_order[idx_output_order] = temp_i+1
            temp_i = temp_i + 1
        else:    # right
            output_order[idx_output_order] = temp_j+1
            temp_j = temp_j - 1
        idx_output_order = idx_output_order + 1

        if temp_i == temp_j:
            output_order[idx_output_order] = temp_j+1

    return int(DP_table[0, array_length-1]), output_order

timber_array = [33, 28, 35, 23, 23, 25, 37, 40, 42, 24, 38, 29, 22, 40, 36, 42, 39, 37, 45, 32]
timber_array = np.asarray(timber_array)

result, output_order = timberDPAlgoTraceback(timber_array)

print(result)
print(' '.join(map(str, output_order)))    # without comma
