########## Lecture 2 lesson handout
def bind_x():
    # Sets x to 3, squares it, and prints the result
    x = 3
    x = x*x
    print(x)
    # Takes user input, stores it in 'n', and prints 'n'
    n = int(input('Enter a number: '))
    print(n)

def check_odd_even():
    # Sets x to 15 and checks if it's even or odd, then prints the result
    x = 15
    if (x/2)*2 == x:
        print('Even')
    else:
        print('Odd')

def define_z():
    # Sets z to 'b' and checks if 'x' is less than 'z', then prints messages
    z = 'b'
    if 'x' < z:
        print('Hello')
        print('Mom')

def find_lowest():
    # Sets x, y, and z, then finds and prints the smallest value among them
    x = 15
    y = 5
    z = 11
    print(x, y, z)
    if x < y and x < z:
        print('x is least')
    elif y < x and y < z:
        print('y is least')
    else:
        print('z is least')

def iterate_left():
    # Initializes y, x, and itersLeft, then iteratively updates and prints them
    y = 0
    x = 3
    itersLeft = x
    while(itersLeft > 0):
        y = y + x
        itersLeft = itersLeft - 1
        print('y =', y, ',itersLeft =', itersLeft)
    print(y)

def divisor():
    # Sets x to 10, finds and prints its divisors
    x = 10
    i = 1
    while(i < x):
        if x%i == 0:
            print('divisor', i)
        i = i + 1
