'''
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number. The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

Extras:

Use binary search.
'''

import math


def binary_search(arr, num):
    start = 0
    end = len(arr) - 1

    while(start <= end):
        mid = math.floor((end + start) // 2)
        mid_value = arr[mid]

        if (mid_value == num):
            return True
        if (mid_value > num):
            end = mid-1
        else:
            start = mid + 1

    return False


a = [1, 2, 3, 4, 6, 7, 8, 9, 15, 17]
print(binary_search(a, 4))
