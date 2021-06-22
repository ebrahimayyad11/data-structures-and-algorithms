def multi_bracket_validation(input):
    brackets_open = ['(','{','[']
    brackets_open_counter = [0,0,0]
    brackets_close = [')','}',']']
    brackets_close_counter = [0,0,0]

    arr = list(input)
    new_arr = []
    for i in arr:
        if i in brackets_close or i in brackets_open:
            new_arr += i

    for i in range(len(new_arr)):
        for j in range(len(brackets_close)):
            if new_arr[i] == brackets_close[j]:
                brackets_close_counter[j] += 1
                if (brackets_close_counter[j] > brackets_open_counter[j]):
                    return False 
                elif new_arr[i-1] in brackets_open and not new_arr[i-1] == brackets_open[j]:
                    return False
            elif new_arr[i] == brackets_open[j]:
                brackets_open_counter[j] += 1

    counter = 0
    for i in range(len(brackets_close)):  
        if brackets_open_counter[i] == brackets_close_counter[i]:
            counter += 1

    return counter == 3
