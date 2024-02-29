def remove_duplicates_and_sort(arr):
    unique_arr = []
    for num in arr:
        if num not in unique_arr:
            unique_arr.append(num)
    unique_arr.sort()
    return unique_arr
input_list = [15,14,25,14,32,14,31]
result = remove_duplicates_and_sort(input_list)
print(result)
