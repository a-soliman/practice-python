'''
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
'''

import random


def generate_password(length=6):
    symbols = ["!", "@", "#", "$", "%", "&", "<", ">"]
    lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
             "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    upper = [x.upper() for x in lower]
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    content = [symbols, lower, upper, nums]
    password = ""
    for i in range(length):
        group = random.randint(0, len(content)-1)

        random_content = content[group]
        random_num = random.randint(0, len(random_content)-1)
        random_char = random_content[random_num]
        password += random_char

    return password


print(generate_password(10))
