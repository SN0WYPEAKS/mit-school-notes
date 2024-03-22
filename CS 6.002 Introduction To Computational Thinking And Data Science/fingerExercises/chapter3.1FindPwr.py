class findPwr:
    def getUserInput(userInt):
        userInput = input("Enter a positive integer: ")
        while userInt < 0:
            userInt = userInput
            print("Oh my bad... I thought I said to enter a POSITIVE integer. Try it again!")