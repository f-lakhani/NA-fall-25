import numpy as np

#defining the function
def f(x):
    #QUESTION 1: f(x) = x^2 - 2
    #return np.pow(x, 2) - 2

    #QUESTION 2: f(x) = exp(-x) - x
    return np.exp(-x) - x

def secant_method(x0, x1, max_iterations=100):
    # no tolerance parameter since tolerance not defined in the question
    #print header for output table
    print(f"{'Iteration':<10}{'x1':<20}{'x2':<20}{'f(x)':<20}")
    print("-" * 70)

    for i in range(max_iterations):
        f_x0 = f(x0)
        f_x1 = f(x1)
    
        if abs(f_x1 - f_x0) < 1e-11:  #float numbers are rarely exact 0, so check whether division by 0 occurs using 1e-11 instead
            print("division by 0. Secant method fails.")
            return None
        
        # Formula for secant method. Find x2.
        x2 = x1 - f_x1 * (x1-x0) / (f_x1 - f_x0)

        # Print iteration details
        print(f"{i:<10}{x1:<20.10f}{x2:<20.10f}{f(x2):<20.10f}")

        if abs(f(x2)) < 1e-11: # float numbers are rarely exact 0, so check convergence with 1e-11 instead
            print(f"\nExact root found: {x2}")
            return x2
        #update interval for next iteration
        x0 = x1 
        x1 = x2

    #max iterations reached but exact root not found
    print(f"\nApproximate root after {max_iterations} iterations: {x2}")
    return x2

#initial guesses
# QUESTION 1
#x0 = 1
#x1 = 2

#QUESTION 2
x0 = 0
x1 = 2

root = secant_method(x0, x1)
if root is not None:
    print(f"Root found: {round(root, 3)}")
else:
    print("No root found.")