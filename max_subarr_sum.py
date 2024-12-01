

def max_subarr_sum(arr, k):
    result_sum = 0
    
    for j in range(len(arr)-k+1):
        sub_arr = arr[j:(j+k)]
        arr_sum = sum(sub_arr)

        if result_sum < arr_sum:
            result_sum = arr_sum

        print(sub_arr, arr_sum)

    return result_sum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
k = 4


arr2 = [2, 4, 10, 4, 20, 1, 9, 4, 23]
k2 = 4

print(f'\n Result 1 = {max_subarr_sum(arr, k)}\n')
print(f'\n Result 2 = {max_subarr_sum(arr2, k2)}\n')