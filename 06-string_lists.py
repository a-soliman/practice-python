'''
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

Discussion
Concepts for this week:

List indexing
Strings are lists
'''


def is_palindrome(s):
    return s == "".join(reversed(s))


def get_input():
    s = input("Please provide a string: ")
    print(is_palindrome(s))


get_input()
