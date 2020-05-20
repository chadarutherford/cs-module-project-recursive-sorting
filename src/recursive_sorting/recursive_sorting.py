# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(left, right):
    # init the combined list
    # that will hold the sorted elements from left and right
    combined = []

    #init the pointers that start at the beginning of each list
    a = 0
    b = 0

    # traverse the lists
    while a < len(left) and b < len(right):
        # compare elements from pointers
        if left[a] < right[b]:
            combined.append(left[a])
            a += 1
        else:
            combined.append(right[b])
            b += 1

    # at this point, we have finished traversing one list completely
    # we need to add all of the elements from the other list to the combined list
    while a < len(left):
        combined.append(left[a])
        a += 1
    while b < len(right):
        combined.append(right[b])
        b += 1

    return combined

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # break the array down recursively
    # base case: when the list gets down to single elements
    if len(arr) > 1:
        # break down array halves until they reach the point
        # where we have arrays of single elements
        left = merge_sort(arr[:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])

        # merge them back up
        arr = merge(left, right)

    return arr
    
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