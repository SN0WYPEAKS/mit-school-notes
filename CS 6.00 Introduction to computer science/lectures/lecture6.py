########## Lecture 6 lesson handout

# Function to calculate square root using the binary search method
def squareRootBi(x, epsilon):
    """Assumes x >= 0 and epsilon > 0
    Return y s.t. y*y is within epsilon of x"""
    assert x >= 0, 'x must be non-negative, not ' + str(x)
    assert epsilon > 0, 'epsilon must be positive, not ' + str(epsilon)
    # Initialize low and high for binary search
    low = 0
    high = max(x, 1.0)
    guess = (low + high)/2.0
    ctr = 1
    while abs(guess**2 - x) > epsilon and ctr <= 100:
        #print('low:', low, 'high:', high, 'guess:', guess)
        # Binary search iteration
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high)/2.0
        ctr += 1
    assert ctr <= 100, 'Iteration count exceeded'
    print('Bi method. Num. iterations:', ctr, 'Estimate:', guess)
    return guess

def testBi():
    print('squareRoot(4, 0.0001)')
    squareRootBi(4, 0.0001)
    print('squareRoot(9, 0.0001)')
    squareRootBi(9, 0.0001)
    print('squareRoot(2, 0.0001)')
    squareRootBi(2, 0.0001)
    print('0.25, 0.0001')
    squareRootBi(0.25, 0.0001)

# Function to calculate square root using the Newton-Raphson method
def squareRootNR(x, epsilon):
    """Assumes x >= 0 and epsilon > 0
       Return y s.t. y*y is within epsilon of x"""
    assert x >= 0, 'x must be non-negative, not ' + str(x)
    assert epsilon > 0, 'epsilon must be positive, not ' + str(epsilon)
    x = float(x)
    guess = x/2.0
    guess = 0.001
    diff = guess**2 - x
    ctr = 1
    while abs(diff) > epsilon and ctr <= 100:
        #print('Error:', diff, 'guess:', guess)
        guess = guess - diff/(2.0*guess)
        diff = guess**2 - x
        ctr += 1
    assert ctr <= 100, 'Iteration count exceeded'
    print('NR method. Num. iterations:', ctr, 'Estimate:', guess)
    return guess

def compareMethods():
    print('squareRoot(2, 0.01)')
    squareRootBi(2, 0.01)
    squareRootNR(2, 0.01)
    input()
    print('squareRoot(2, 0.0001)')
    squareRootBi(2, 0.0001)
    squareRootNR(2, 0.0001)
    input()
    print('squareRoot(2, 0.000001)')
    squareRootBi(2, 0.000001)
    squareRootNR(2, 0.000001)
    input()
    print('squareRoot(1234567890, 0.0001)')
    squareRootBi(1234567890, 0.0001)
    squareRootNR(1234567890, 0.0001)
    input()
    print('squareRoot(1234567890, 0.0000001)')
    squareRootBi(1234567890, 0.000001)
    squareRootNR(1234567890, 0.000001)
    input()
    print('squareRoot(2736336100, 0.0001)')
    squareRootBi(2736336100, 0.0001)
    squareRootNR(2736336100, 0.0001)
    input()

# Function to demonstrate list operations
def showLists():
    Techs = ['MIT', 'Cal Tech']
    print(Techs)
    input()
    Ivys = ['Harvard', 'Yale', 'Brown']
    print(Ivys)
    input()
    Univs = []
    Univs.append(Techs)
    print(Univs)
    input()
    Univs.append(Ivys)
    print(Univs)
    input()
    for e in Univs:
        print(e)
        for c in e:
            print(c)
    input()
    Univs = Techs + Ivys
    print(Univs)
    input()
    Ivys.remove('Harvard')
    print(Univs)
    input()
    Ivys[1] = str(-1)
    print(Ivys)
    input()

    L1 = [1, 2, 3]
    L2 = L1
    L1[0] = 4
    print(L2)
    input()

    def f(L):
        L[0] = 4
    L1 = [1,2,3]
    L2 = [1,2,3]
    L3 = L1
    print(L1 == L2)
    f(L1)
    print(L1 == L2)
    print(L1)
    print(L2)
    print(L3)

    L1 = [1,2,3]
    L2 = L1[:] # makes a copy of L1
