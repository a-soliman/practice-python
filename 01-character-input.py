'''
Character Input 
input strings types int
Calibrating the exercises to the audience is going to be a challenging task, so I ask you to bear with me if the exercises are too easy or too hard. Every week there will be a poll you can click on to discuss whether the exercise is too easy or too hard and hopefully in a few weeks, I’ll get the level right. Let’s get to it! I will start with the exercise and include a discussion later, in case you want the extra challenge.

Exercise 1 (and Solution)
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
'''

import datetime


def main():
    name = get_name()
    age = get_age()
    copys = get_copys_num()
    hundred_on = get_year_100(age)
    return message(name, hundred_on, copys)


def get_name():
    return input("What's your name? :")


def get_age():
    return int(input("How old are you? :"))


def get_copys_num():
    return int(input("Provide copys num: "))


def get_year_100(age):
    current_year = datetime.datetime.now().year
    return (100 - age) + current_year


def message(name, hundred_on, copys):
    message = f"{name}, you'll be a 100 years old on ${hundred_on}\n"
    print(message*copys)
    return


main()
