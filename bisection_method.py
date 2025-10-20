import numpy as np

def f(x):
    # function to be evaluated
    #QUESTION 1: f(x) = x^3-4x^2+6x-24
    #return np.power(x,3)-4*np.power(x, 2)+6*x-24
    # QUESTION 2: f(x) = sin(x) - 0.5
    return np.sin(x)- 0.5

def bisection_method(a, b, max_iterations = 60):
    """
    parameters:
     a: float - lower bound of interval
     b: float - upper bound of interval
     no tolerance because none given in question
     max_iterations: to prevent infinite loop
     returns a float representing the approximate or exact root of the function
    """
    if f(a)*f(b) > 0:
        #checking if IVT applies and root exists in interval
        raise ValueError("f(a)*f(b) > 0 so by IVT no root exists in this interval.")

    it = 0 #track iterations
    #print header for output table
    print(f"{'Iteration':<10}{'a':<20}{'b':<20}{'Midpoint':<20}{'f(Midpoint)'}")
    print("-" * 85)
    # continue till either exact root found or max iterations reached  
    while it < max_iterations:
        midpoint = (a+b) / 2.0 #calculate new midpoint
        
        #print iteration details
        print(f"{it:<10}{a:<20.10f}{b:<20.10f}{midpoint:<20.10f}{f(midpoint):.10f}")

        # convergence check to 1e-11 since floating point numbers are rarely exact 0, so f(midpoint) == 0 won't work
        if abs(f(midpoint)) < 1e-11:
            print(f"\nExact root found: {midpoint}")
            return midpoint
        elif f(a)*f(midpoint)<0: # update interval to narrow search after each iteration. IVT must apply.
            b = midpoint
        else:
            a = midpoint

        it += 1
    print(f"Did not converge.") # If maximum iterations reached and root wasnt found
    return None

try:
    #question 1
    #root = bisection_method(2, 4)
    #question 2
    root = bisection_method(0, 1)
    print(f"root: {round(root, 3)}")
    
except ValueError as e:
    print(e)

