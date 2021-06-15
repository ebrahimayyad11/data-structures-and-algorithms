

def kth (k):
    arr = [1,3,8,2]
    if k >= len(arr) or k < 0:
        return Exception
    else:
        new_arr = arr[::-1]
        return new_arr[k]
