########## Lecture 3 lesson handout
# Find the square root of a perfect square
# Basic code that only checks for perfect square with no other checks
def find_nearest_perfect_square():
    # Initialize the number for which we want to find the nearest perfect square.
    x = 15
    # Initialize the variable to store the result
    ans = 0
    # Start a loop to increment 'ans' until its square equals or surpasses 'x'
    while ans*ans < x:
        ans = ans + 1
    # Print the integer 'ans', which is the nearest perfect square to 'x'
    print(ans)

# Checks if x has a perfect square or if it is negative, if not, informs the user of the issue
def perfect_square_test():
    # Initialize a variable to store the result
    ans = 0
    # Takes user input to check if the number input has a perfect square
    x = int(input("Please enter a number to check if it can be perfectly squared: "))
    # Checks if the number is non-negative
    if x >= 0:
        # Start a loop to increment 'ans' until its square is less than 'x'
        while ans*ans < x:
            ans = ans + 1
            print('ans =', ans)
        # Check if 'x' is a perfect square or not and output the result accordingly
        if ans*ans != x:
            print(x, 'is not a perfect square')
        else:
            print(ans)
    else:
        # Executed if the input number is negative
        print(x, 'is a negative number')

# Example of a while loop in use
def divisor_while_loop():
    x = 10
    i = 1
    while(i<x):
        if x%i == 0:
            print('divisor ', i)
        i = i + 1

# Example of a for loop replacing the while loop
def divisor_for_loop():
    # Initialize x with a value of 100
    x = 100
    # Create an empty list 'divisors' to store the divisors of 'x'.
    divisors = []
    # Iterate through numbers from 1 to 'x-1' using a for loop
    for i in range(1, x):
        # Check if 'i' is a divisor of 'x' (i.e., 'x' is divisible by 'i')
        if x%i == 0:
            # If 'i' is a divisor, add it to the 'divisors' list
            divisors = divisors + [i]

# This function calculates the sum of individual digits in the integer 1952
def addition_of_ints():
    sumDigits = 0
    # Converts the int 1952 into a string
    for c in str(1952):
        # Converts the string back into an int and adds the individual ints together
        sumDigits += int(c)
    # The output will be 1 + 9 + 5 + 2 = 17
    print(sumDigits)
