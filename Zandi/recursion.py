def sum_array(array):
    '''Return sum of all items in array'''
    sums=0
    for i in array:
        sums=sums+i
    return sums

def fibonacci(n):
    '''Return nth term in fibonacci sequence'''
    if  n<=2:
        return 1
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)
def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)

def reverse(word):
    '''Return word in reverse'''
    rev_word=''
    for i in word:
        rev_word=i+rev_word
    return rev_word
