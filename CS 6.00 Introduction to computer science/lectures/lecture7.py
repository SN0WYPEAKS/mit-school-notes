########## Lecture 7 lesson handout

import math

def getRightTriangle():
    # Code in the handout that did not work
    # Get base
    # inputOK = False
    # while not inputOK:
    #     base = input('Enter base: ')
    #     if type(base) == type(1.0): inputOK = True
    #     else: print('Error. Base must be floating point number.') 
    # Get base code that has no errors
    inputOK = False
    while not inputOK:
        baseStr = input('Enter base: ')
        try:
            base = float(baseStr)
            inputOK = True
        except ValueError:
            print('Error. Base must be floating point number')
    # Code in the handout that did not work
    # Get height
    # inputOK = False
    # while not inputOK:
    #     height = input('Enter height: ')
    #     if type(height) == type(1.0): inputOK = True
    #     else: print('Error. Height must be floating point number.')
    # Get height code that has no errors
    inputOK = False
    while not inputOK:
        heightStr = input('Enter height: ')
        try:
            height = float(heightStr)
            inputOK = True
        except ValueError:
            print('Error. Height must be floating point number.')
    hyp = math.sqrt(base*base + height*height)
    print('Base: ' + str(base) + ', height: ' + str(height) + ', hyp: ' + str(hyp))

def getFloat(requestMsg, errorMsg):
    inputOK = False
    while not inputOK:
        val = input(requestMsg)
        if type(val) == type(1.0):
            inputOK = True
        else:
            print(errorMsg)
    return val

def expl(a,b):
    ans = 1
    while(b>0):
        ans *= a
        b -= 1
    return ans

def exp2(a,b):
    if b == 1:
        return a
    else:
        return a*exp2(a,b-1)
    
def exp3(a,b):
    if b == 1:
        return a
    if (b%2) * 2 == b:
        return exp3(a*a,b/2)
    else:
        return a*exp3(a,b-1)
    
def g(n):
    x = 0
    for i in range(n):
        for j in range(n):
            x += 1
    return x

def Towers(size, fromStack, toStack, spareStack):
    if size == 1:
        print('Move disk from ',fromStack, 'to ', toStack)
    else:
        Towers(size-1, fromStack, spareStack, toStack)
        Towers(1, fromStack, toStack, spareStack)
        Towers(size-1, spareStack, toStack, fromStack)
