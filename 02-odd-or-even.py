'''
Odd Or Even 
input if types int equality comparison numbers mod
Again, the exercise comes first (with a few extras if you want the extra challenge or want to spend more time), followed by a discussion. Enjoy!

Exercise 2 (and Solution)
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
'''


def main():
    user_num = get_user_num()
    is_even = False

    if user_num % 2 == 0:
        is_even = True

        if user_num % 4 == 0:
            return message(is_even, "multiple of 4")

    return message(is_even)


def get_user_num():
    return int(input("Please provide a number: "))


def message(isEven, multiple_of_4=False):

    if multiple_of_4:
        print("multiple of 4")
    elif not multiple_of_4 and isEven:
        print("Even num")
    else:
        print("Odd num")


main()
