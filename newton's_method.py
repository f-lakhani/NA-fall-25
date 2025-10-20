import numpy as np

# Define the function
def func(x):
    # QUESTION 1: f(x) = x^4 - 2x^3 + x - 1
    #return np.pow(x, 4) - 2 * np.pow(x, 3) + x - 1

    #QUESTION 2: f(x) = tan(x) - x
    return np.tan(x) - x

# Define the function's derivative
def derivative(x):
    #Q1
    #return 4* np.pow(x, 3) - 6 * pow(x, 2) + 1
    #Q2
    return 1/np.pow(np.cos(x), 2) - 1

def newton_method(x0, max_iter=100):
    # no tolerance parameter since it isn't given in the question
    x = x0
    #print header for output table
    print(f"{'Iteration':<10}{'x':<20}{'f(x)':<20}{'f\'(x)':<20}")
    print("-" * 70)
    # print initial guess
    print(f"{0:<10}{x0:<20.10f}{func(x0):<20.10f}{derivative(x0):<20.10f}")

    for i in range(1, max_iter+1):
        f_x = func(x)
        df_x = derivative(x)

        #float numbers are rarely exact 0, so check whether division by 0 occurs using 1e-11 instead
        if abs(df_x) < 1e-11:
            print("Derivative is zero, so Newton's method fails.")
            return None
        
        h = f_x / df_x
        x = x - h #update value of x_n
        
        # Print iteration details
        print(f"{i:<10}{x:<20.10f}{func(x):<20.10f}{derivative(x):<20.10f}")
        # float numbers are rarely exact 0, so check convergence with 1e-11 instead
        if abs(func(x)) < 1e-11:
            print(f"\nConvergence reached: x = {x}")
            return x
    
    print("\nMaximum iterations reached without convergence.")
    return None


x0 = 1
root = newton_method(x0)
if root is not None:
    print(f"Root found: {round(root, 3)}")
else:
    print("No root found.")

