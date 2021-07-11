# Blog for Code Challenge 26 - Insertion Sort
## Description
Selection Sort is a sorting algorithm in the same family as bubble sort and selection sort but simpler and more efficient. Selection sort works by iterating across the array starting at the front and comparing if the value of the element next to it is lower. If the next door value is lower the elements change places.
### Pseudocode
```pseudocode
InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
```
### Python3 Implementation
```python3
def InsertionSort(arr):

    for i in range(len(arr)):

      j = i - 1
      temp = arr[i]

      while j >= 0 and temp < arr[j]:
        arr[j + 1] = arr[j]
        j = j - 1

      arr[j + 1] = temp
    return arr
```
## Trace
### Pass 1
![Pass 1](./img/selectionSort1.png)
 We find this smaller number right away in index 1. The minimum value gets updated to remember this index. At the end of the evaluation, the smaller number will be swapped with the current value in index i. This results in our smallest number of our array being placed first.
### Pass 2
![Pass 2](./img/selectionSort2.png)
The second pass through the array evaluates the remaining values in the array to see if there is a smaller value other than the current position of i. 8 is the 2nd smallest number in the array, so it “swaps” with itself. The minimum value does not change at all during the iteration of this pass.
### Pass 3
![Pass 3](./img/selectionSort3.png)
The third pass through evaluates the remaining indexes in the array, starting at position 2. Both position 4 and 5 are smaller than the value in position 2. Each time a smaller number than the current minimum is found, the variable will update to the new smallest number. In this case, 15 is the next smallest number. As a result, it will swap with position 2.
### Pass 4
![Pass 4](./img/selectionSort4.png)
The 4th pass through on the array proves that 16 is the next smallest number in the array, and as a result, switches places with the 42.
### Pass 5
![Pass 5](./img/selectionSort5.png)
The 5th pass through of the array only has one other index to evaluate. Since the last index value is larger than index 4, the two values will swap.
### Pass 6
![Pass 6](./img/selectionSortFinal.png)
On its final iteration through the array, it will swap places with itself as it evaluates the value against itself.
After this iteration, i will increment to 6, forcing it to break out of the outer for loop and leaving our array now sorted.