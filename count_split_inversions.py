split_invs = 0

def mergeSort(a_list):
    if len(a_list) <= 1:
        return a_list

    mid = len(a_list) // 2
    left = a_list[:mid]
    right = a_list[mid:]

    return merge_and_count(mergeSort(left), mergeSort(right));


def merge_and_count(left, right):
    global split_invs
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
            split_invs += (len(left) - l_index)

    while l_index < len(left):
        merged_list.append(left[l_index])
        l_index += 1
    while r_index < len(right):
        merged_list.append(right[r_index])
        r_index += 1

    return merged_list


print mergeSort([6, 5, 4, 3, 2, 1])
print split_invs
