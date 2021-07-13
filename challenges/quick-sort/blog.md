# Blog for Code Challenge 28 - Quick Sort

## Description

Quick sort is similar to merge sort, in that it's a conquer and divide style sorting algorithm. It chooses a pivot value and partitions the input array into a left and right array. The main difference between merge sort and quick sort is that by the time quick sort has broken up the array into sub arrays of single elements the array is sorted.

### Pseudocode

```pseudocode
ALGORITHM QuickSort(arr, left, right)
    if left < right
        // Partition the array by setting the position of the pivot value
        DEFINE position <-- Partition(arr, left, right)
        // Sort the left
        QuickSort(arr, left, position - 1)
        // Sort the right
        QuickSort(arr, position + 1, right)

ALGORITHM Partition(arr, left, right)
    // set a pivot value as a point of reference
    DEFINE pivot <-- arr[right]
    // create a variable to track the largest index of numbers lower than the defined pivot
    DEFINE low <-- left - 1
    for i <- left to right do
        if arr[i] <= pivot
            low++
            Swap(arr, i, low)

     // place the value of the pivot location in the middle.
     // all numbers smaller than the pivot are on the left, larger on the right.
     Swap(arr, right, low + 1)
    // return the pivot index point
     return low + 1

ALGORITHM Swap(arr, i, low)
    DEFINE temp;
    temp <-- arr[i]
    arr[i] <-- arr[low]
    arr[low] <-- temp
```

### Python3 Implementation

```python3
def QuickSort(arr, left=None, right=None):
    if len(arr) == 0 or len(arr) == 1:
      return arr
    else:
      if left == None and right == None:
        left = 0
        right = len(arr) - 1
      if left < right:
        # Partition the array by setting the position of the pivot value
        position = Partition(arr, left, right)
        # Sort the left
        QuickSort(arr, left, position - 1)
        # Sort the right
        QuickSort(arr, position + 1, right)

        return arr

def Partition(arr, left, right):
    # set a pivot value as a point of reference
    pivot = arr[right]
    # create a variable to track the largest index of numbers lower than the defined pivot
    low = left - 1
    for i in range(left, right):
        if arr[i] <= pivot:
            low += 1
            Swap(arr, i, low)

    # place the value of the pivot location in the middle.
    # all numbers smaller than the pivot are on the left, larger on the right.
    Swap(arr, right, (low + 1))
    # return the pivot index point
    return low + 1

def Swap(arr, i, low):
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp
```

## Trace

`arr = [8,4,23,42,16,15]`

Indexes: 0 1 2 3 4 5

left = 0,  
right = 5,  
pivot = arr[right] = 15  
low = left - 1 = -1

loop from `left` to `right-1`  
i = 0 : Since `arr[i] <= pivot` = `8 <= 15`
which returns True, Then `low += 1`
`swap (arr,i,low)`

`arr = [8,4,23,42,16,15]`

i = 1 : Since `arr[i] <= pivot` = `4 <= 15` ,
which returns True, Then `low += 1`
`swap (arr,i,low)`

`arr = [8,4,23,42,16,15]`

i = 2 : Since `arr[j] <= pivot` = `23 <= 15`, which returns False,then i++

`arr = [8,4,23,42,16,15]`

i = 3 : Since `arr[j] > pivot` = `42 <= 15`, which returns False,then i++

`arr = [8,4,23,42,16,15]`

i = 4 : Since `arr[j] > pivot` = `16 <= 15`, which returns False,then i++

`arr = [8,4,23,42,16,15]`

i = 5 : Since `arr[i] <= pivot` = `15 <= 15` ,
which returns True, Then `low += 1`
`swap (arr,5,2)`

`arr = [8,4,15,42,16,23]`

`swap(arr,right,low+1) = swap(arr,5,3)`

`arr = [8,4,15,23,16,42]`

then it will return the low+1 = 3

then it will call the same function 2 times one for the left side and one for the right side

`Quicksort(arr,left,position -1) = Quicksort(arr,0,2)`

`Quicksort(arr,position +1,right) = Quicksort(arr,4,5)`

and it will redo the same operations that I mentioned above and in the end it will return the array sorted from the lowest number to the highest number 

`arr = [4,8,15,16,23,42]`