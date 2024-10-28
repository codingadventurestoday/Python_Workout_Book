"""Recreate the Sum Function: 
take in a sequence of numbers and return the sum of those numbers
i.e sum[1, 2, 3]  returns 6"""

def my_sum(*args):
    """Takes in an arbritury amount of numbers and returns their sum"""
    sum = 0
    for i in args:
        if isinstance(i, int) or isinstance(i, float):
            sum += i
    return sum

print(my_sum())