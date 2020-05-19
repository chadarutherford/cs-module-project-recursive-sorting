# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # creating an empty array in memory for storage
    merged_arr = [0] * elements
    # compare first elements
    a = 0
    b = 0

    # loop through all the elements
    for i in range(0, elements):
        # if a is greater than the length of the first half of the split array
        if a >= len(arrA):
            # set the merged array's i'th index equal to the b'th index in array B
            merged_arr[i] = arrB[b]
            # increment B
            b += 1
        elif b >= len(arrB):
            # set the merged array's i'th index equal to the a'th index in array A
            merged_arr[i] = arrA[a]
            # increment A
            a += 1
        elif arrA[a] < arrB[b]:
            # set the merged array's i'th index equal to the a'th index in array A
            merged_arr[i] = arrA[a]
            # increment A
            a += 1
        else:
            # set the merged array's i'th index equal to the b'th index in array B
            merged_arr[i] = arrB[b]
            # increment B
            b += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # make copies of both arrays that we are trying to merge
    # second parameter is non-inclusive so we need to add 1
    left_array = arr[start: mid + 1]
    right_array = arr[mid + 1: end + 1]

    # set up initial values to keep track of progress through array
    left_index = 0
    right_index = 0
    sorted_index = start

    # iterate through both copies until we have no elements left in one of them
    while left_index < len(left_array) and right_index < len(right_array):
        # if the left side has the smaller element
        # place it in the sorted part and move left_array forward
        if left_array[left_index] <= right_array[right_index]:
            arr[sorted_index] = left_array[left_index]
            left_index += 1
        else:
            arr[sorted_index] = right_array[right_index]
            right_index += 1
        sorted_index += 1

    # here we have no elements in left or right
    # go through remaining elements and add them
    while left_index < len(left_array):
        arr[sorted_index] = left_array[left_index]
        left_index += 1
        sorted_index += 1

    while right_index < len(right_array):
        arr[sorted_index] = right_array[right_index]
        right_index += 1
        sorted_index += 1
    return arr


def merge_sort_in_place(arr, left, right):
    if left >= right:
        return arr

    mid = (left + right) // 2
    merge_sort_in_place(arr, left, mid)
    merge_sort_in_place(arr, mid + 1, right)
    merge_in_place(arr, left, mid, right)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr