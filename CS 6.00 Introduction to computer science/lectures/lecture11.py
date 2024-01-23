########## Lecture 11 lesson handout

def silly():
    res = []
    done = False
    while not done:
        elem = input('Enter element. Return when done. ')
        if elem == '':
            done = True
        else:
            res.append(elem)
    #print("res: should be [1, 'a', 2]:", res)
    #old code
    #tmp = res(points to the list)
    tmp = res[:]#(makes a clone of the list)
    #print('tmp', tmp, 'res', res)
    tmp.reverse()
    #print('tmp', tmp, 'res', res)
    isPal = (res == tmp)
    #print('tmp', tmp, 'res', res)
    if isPal:
        print('is a palindrome')
    else:
        print('is NOT a palindrome')
