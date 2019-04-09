'''
Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.
'''


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def get_num():
    num = int(input("Please provide a number: "))
    return is_prime(num)


print(get_num())
