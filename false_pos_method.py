import numpy as np
def f(x):
    # function to be evaluated

    # QUESTION 1: f(x) = ln(x) - 1
    #return np.log(x) - 1

    # QUESTION 2: f(x) = exp(x) - 5
    return np.exp(x) - 5

def false_position_method(a, b, max_iterations = 100):
    """
    parameters:
     a: float - lower bound of interval
     b: float - upper bound of interval
     no tolerance because none given in question
     max_iterations: to prevent infinite loop
     returns a float representing the approximate / exact root of the function
    """
    if f(a)*f(b) > 0: # check if IVT applies to ensure root exists in interval
        raise ValueError("f(a)*f(b) > 0 so by IVT no root exists in this interval.")

    it = 0 # track iterations
    #print header for output table
    print(f"{'Iteration':<10}{'a':<20}{'b':<20}{'c':<20}{'f(c)'}")
    print("-" * 85)
    
    # keep iterating till root found or maximum iterations reached
    while it < max_iterations:
        #float numbers are rarely exact 0, so check whether division by 0 occurs using 1e-11 instead
        if abs(f(b)-f(a)) < 1e-11:
            print("Denominator is zero, so False position method fails.")
            return None
          
        # calculate point c
        c = (a*f(b) - b*f(a)) / (f(b) - f(a))
        
        # print iteration details
        print(f"{it:<10}{a:<20.10f}{b:<20.10f}{c:<20.10f}{f(c):.10f}")
        
        # convergence check to 1e-11 since floating point numbers are rarely exact 0, so f(c) == 0 won't work
        if abs(f(c)) < 1e-11:
            print(f"\nExact root found: {c}")
            return c
        elif f(a)*f(c)<0:
            b = c
        else:
            a = c

        it += 1
    print(f"Did not converge.") # If maximum iterations reached and root wasnt found
    return None

try:
    #QUESTION 1
    #root = false_position_method(1, 3)
    
    #QUESTION 2
    root = false_position_method(0, 2)
    print(f"root: {round(root, 3)}")
    
except ValueError as e:
    print(e)

