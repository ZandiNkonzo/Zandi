def fibonacci(n):
    '''Return nth term in fibonacci sequence'''
    if  n>2:
        return fibonacci(number - 2) + fibonacci(number - 1)
    else:
        return 1
def sum_array(array):
    '''Return sum of all items in array'''
    sums=0
    for i in array:
        sums=sums+i
    return sums

def factorial(n):
    '''Return n!'''
    my_arr=[]
    for i in range(1,n+1,1):
        my_arr.append(i)
    factorial=0
    #sum_array(my_arr)
    for k in my_arr:
        factorial=factorial+k
    return factorial

def reverse(word):
    '''Return word in reverse'''
    rev_word=''
    for i in word:
        rev_word=i+rev_word
    return rev_word
