def bubble_sort(items):
    '''Return array of items, sorted in ascending order'''
    arr = items.copy() # make copy of given array
    length=len(arr)# find lenght of array
    for i in range(length): # take the first position element
        for k in range(length-1-i): # compare element with the rest of the elements
            if arr[k] > arr[k+1]: #check if there is any element bigger and swap them around
                arr[k], arr[k+1] = arr[k+1], arr[k]     # Swap

    return arr

def merge_sort(items):
    '''Return array of items, sorted in ascending order'''
    new_list = []
    if len(items)== 1:
        return items
    mid_point = int(len(items) / 2)
    A = merge_sort(items[:mid_point])
    B= merge_sort(items[mid_point:])
    while len(A) > 0 and len(B) > 0:
        if A[0] < B[0]:
            new_list.append(A[0])
            A.pop(0)
        else:
            new_list.append(B[0])
            B.pop(0)

    if len(A) == 0:
        new_list = new_list + B
    if len(B) == 0:
        new_list = new_list + A

    return new_list

def quick_sort(items):
    '''Return array of items, sorted in ascending order'''
    len_i = len(items)
    if len_i <= 1: # if we only have one or less numbers return that one character
        return items
    same = [] # all the numbers that are the same as the index number
    small = [] # an array for numbers smaller than index
    big = [] # array for numbers bigger than index
    index = items[-1] # use last value as index

    for i in items: #put numbers smaller in small array
        if i < index:
            small.append(i)
        elif i > index: # put numbers bigger in big array
            big.append(i)
        elif i == index: # all same numbers as index in the same array
            same.append(i)

    small = quick_sort(small) # further sort the small array by above method
    large = quick_sort(big) # further sort big array with above method

    return small + same + large
