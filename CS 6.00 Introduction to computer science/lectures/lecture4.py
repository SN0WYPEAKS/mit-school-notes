########## Code for lecture 4 in 6.00 Mit programming class
#example code for finding square roots
x = 16
ans = 0

# Find the square root of x using a while loop
if x >= 0:
    while ans*ans < x:
        ans = ans + 1
        print('ans =', ans)
    if ans*ans != x:
        print(x, 'is not a perfect square')
    else:
        print(ans)
else:
    print(x, 'is a negative number')

# Define a function to calculate the square root of a number
def sqrt(x):
    """Returns the square root of x, if x is a perfect square. Prints an error message and returns None otherwise"""
    ans = 0
    if x >= 0:
        while ans*ans < x: ans - ans + 1
        if ans*ans != x:
            print(x, 'is not a perfect square')
            return None
        else:
            return ans
    else:
        print(x, 'is a negative number')
        return None

# Define a function f that increments the input by 1
def f(x):
    x = x + 1
    return x

x = 3
z = f(x)
print(x)
print(z)

# Code for finding the number of different animals based on head count and leg count
# Three versions of the solve function are provided

# Version 1
def solve(numLegs, numHeads):
    for numChicks in range(0, numHeads + 1):
        numPigs = numHeads - numChicks
        totLegs = 4*numPigs + 2*numChicks
        if totLegs == numLegs:
            return (numPigs, numChicks)
    return(None, None)

def barnYard():
    heads = int(input('Enter number of heads: '))
    legs = int(input('Enter number of legs: '))
    pigs, chickens = solve(legs, heads)
    if pigs == None:
        print('There is no solution')
    else:
        print('Number of pigs:', pigs)
        print('Number of chickens:', chickens)

def solve1(numLegs, numHeads):
    for numSpiders in range(0, numHeads + 1):
        for numChicks in range(0, numHeads - numSpiders + 1):
            numPigs = numHeads - numChicks - numSpiders
            totLegs = 4*numPigs + 2*numChicks + 8*numSpiders
            if totLegs == numLegs:
                return(numPigs, numChicks, numSpiders)
    return(None, None, None)

# Version 2
def barnYard1():
    heads = int(input('Enter number of heads: '))
    legs = int(input('Enter number of legs: '))
    pigs, chickens, spiders = solve1(legs, heads)
    if pigs == None:
        print('There is no solution')
    else:
        print('Number of pigs:', pigs)
        print('Number of chickens:', chickens)
        print('Number of spiders:', spiders)

# Version 3
def solve2(numLegs, numHeads):
    solutionFound = False
    for numSpiders in range(0, numHeads + 1):
        for numChicks in range(0, numHeads - numSpiders + 1):
            numPigs = numHeads - numChicks - numSpiders
            totLegs = 4*numPigs + 2*numChicks + 8*numSpiders
            if totLegs == numLegs:
                print('Number of pigs: ' + str(numPigs) + ',')
                print('Number of chickens: ' + str(numChicks) + '+')
                print('Number of spiders: ', numSpiders)
                solutionFound = True
    if not solutionFound: print('There is no solution.')

# Check if a string is a palindrome
def isPalindrome(s):
    """Returns True if s is a palindrome and False otherwise"""
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPalindrome(s[1:-1])

# Calculate the Fibonacci sequence for a given input
def fib(x):
    """Return fibonacci of x, where x is a non-negative int"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
