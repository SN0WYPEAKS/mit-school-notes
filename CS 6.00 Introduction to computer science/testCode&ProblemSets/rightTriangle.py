import math

def getRightTriangle():
    # Get base
    inputOK = False
    while not inputOK:
        baseStr = input('Enter base: ')
        try:
            base = float(baseStr)
            inputOK = True
        except ValueError:
            print('Error. Base must be floating point number')
    # Get height
    inputOK = False
    while not inputOK:
        heightStr = input('Enter height: ')
        try:
            height = float(heightStr)
            inputOK = True
        except ValueError:
            print('Error. Height must be floating point number.')
    hyp = math.sqrt(base*base + height*height) # type: ignore
    print('Base: ' + str(base) + ', height: ' + str(height) + ', hyp: ' + str(hyp)) # type: ignore

def getFloat(requestMsg, errorMsg):
    inputOK = False
    while not inputOK:
        val = input(requestMsg)
        if type(val) == type(1.0):
            inputOK = True
        else:
            print(errorMsg)
    return val # type: ignore