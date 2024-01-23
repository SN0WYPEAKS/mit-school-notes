########## Lecture 5 lesson handout

########## Finding the square root using the Bisection method
def squareRootBi(x, epsilon):
    """Return y s.t. y*y is within epsilon of x"""
    assert epsilon > 0, 'epsilon must be positive, not' + str(epsilon) # Check if epsilon is positive
    low = 0 # Initialize low and high values for the binary search
    high = max(x, 1)
    guess = (low + high)/2.0 # Initialize the initial guess for the square root
    ctr = 1 # Initialize a counter for iterations
    while abs(guess**2 - x) > epsilon and ctr <= 100: # Perform a binary search to find the square root within epsilon
        print('low:', low, 'high:', high, 'guess', guess) # Debugging output to display the current state of the search
        if guess**2 < x:
            low = guess
        else:
            high = guess # Adjust the search range based on the guess
        guess = (low + high)/2.0 # Calculate a new guess
        ctr += 1 # Increment the iteration counter
    assert ctr <= 100, 'Iteration count exceeded' # Ensure the iteration count doesn't exceed 100
    print('Bi method. Num. iterations:', ctr, 'Estimate:', guess) # Print the number of iterations and the final estimate
    return guess # Return the estimated square root

########### Finding the square root using the Newton-Raphson formula
def squareRootNR(x, epsilon):
    """Return y s.t. y*y is within epsilon of x"""
    assert epsilon > 0, 'epsilon must be positive, not' + str(epsilon)
    # Convert x to a float for numerical stability
    x = float(x)
    # Initialize the initial guess for the square root
    guess = x/2.0
    # guess = 0.001
    # Initialize a small value for the initial difference
    diff = guess**2 - x
    ctr = 1
    # Perform Newton-Raphson iteration to find the square root within epsilon
    while abs(diff) > epsilon and ctr <= 100:
        # Debugging output to display the current error and guess
        # print('Error:', diff, 'guess:', guess)
        # Update the guess using the Newton-Raphson formula
        guess = guess - diff/(2.0*guess)
        # Recalculate the difference for the updated guess
        diff = guess**2 - x
        ctr += 1
    assert ctr <= 100, 'Iteration count exceeded'
    print('NR method. Num. iterations:', ctr, 'Estimate:', guess)
    return guess