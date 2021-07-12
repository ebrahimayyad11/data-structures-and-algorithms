def Mergesort(arr):
    n = len(arr) 

    if n > 1:
      mid = n//2
      left = arr[:mid]
      right = arr[mid:]
      Mergesort(left)
      Mergesort(right)
      Merge(left, right, arr)

    return arr


def Merge(left, right, arr):
    left_index = 0
    right_index = 0
    arr_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            arr[arr_index] = left[left_index]
            left_index = left_index + 1
        else:
            arr[arr_index] = right[right_index]
            right_index = right_index + 1

        arr_index = arr_index + 1

    if left_index == len(left):
       for item in right[right_index:]:
            arr[arr_index] = item
            arr_index += 1
    else:
       for item in left[left_index:]:
            arr[arr_index] = item
            arr_index += 1