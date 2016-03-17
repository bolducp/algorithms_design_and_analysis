def mergeSort(a_list):
    if len(a_list) <= 1:
        return a_list

    mid = len(a_list) // 2
    left = a_list[:mid]
    right = a_list[mid:]

    return merge(mergeSort(left), mergeSort(right));


def merge(left, right):
    merged_list = []
    l_index = 0
    r_index = 0

    while l_index < len(left) and r_index < len(right):
        if left[l_index] < right[r_index]:
            merged_list.append(left[l_index])
            l_index += 1
        else:
            merged_list.append(right[r_index])
            r_index += 1

    while l_index < len(left):
        merged_list.append(left[l_index])
        l_index += 1
    while r_index < len(right):
        merged_list.append(right[r_index])
        r_index += 1

    return merged_list

print merge([3, 4, 5], [0, 2, 7, 8])
print mergeSort([3, 4, 5, 0, 2, 7, 8, 1])
