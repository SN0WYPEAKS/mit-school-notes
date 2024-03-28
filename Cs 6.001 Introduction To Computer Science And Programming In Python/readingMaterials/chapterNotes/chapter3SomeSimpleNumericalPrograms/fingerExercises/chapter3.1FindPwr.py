# Finger exercise: Write a program that asks the
# user to enter an integer and prints two integers,
# root and pwr, such that 0 < pwr < 6 and root**pwr
# is equal to the integer entered by the user. If
# no such pair of integers exists, it should print
# a message to that effect.

class findPwr:
    def getUserInput(userInt):
        userInput = input("Enter a positive integer: ")
        while userInt < 0:
            userInt = userInput
            print("Oh my bad... I thought I said to enter a POSITIVE integer. Try it again!")