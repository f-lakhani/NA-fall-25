import numpy as np
def g(x):
    #QUESTION 1: sqrt(6 + x)
    #return np.sqrt(6 + x)
    #QUESTION 2: g(x) = 1 + ln(x)
    return 1 + np.log(x)

def fixed_point_iteration(g, x0, max_iteration = 100):
    """
    g is the function g(x) used for iterations.
    x0 is the initial guess. a float value.
    no tolerance parameter because no tolerance defined in the question.
    address risk of infinite loop by having a maximum number of iterations of 100.

    returns the fixed point as a float
    """
    x_n = x0 
    #print header for output table
    print(f"{'Iteration':<10}{'x':<20}{'g(x)':<20}")
    print("-" * 70)
    # print initial guess
    print(f"{0:<10}{x0:<20.10f}{g(x0):<20.10f}")

    for i in range(1, max_iteration + 1):
        x_n1 = g(x_n) # update x_n value
        # Print iteration details
        print(f"{i:<10}{x_n1:<20.10f}{g(x_n1):<20.10f}")

        if abs(x_n1 - x_n) < 1e-11: # checks convergence by checking if x stops changing. Exact 0 is rare with floating point numbers so we use 1e-11.
            print(f"\nExact fixed point found: x = {x_n1}")
            return x_n1
        x_n = x_n1
    print("did not converge")
    return None

x0 = 2  # Initial guess
result = fixed_point_iteration(g, x0)

if result is not None:
    print(f"Fixed point: {round(result, 3)}")

