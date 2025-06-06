# cvxpy_intro.py
"""Volume 2: Intro to CVXPY.
Zeke Wander
Mth420
5/23/25
"""

#Do Lab 16 CVXPY in Volume2.pdf at https://foundations-of-applied-mathematics.github.io/Links to an external site. 

#Problem 6 is optional. You will likely need to run `pip install cvxpy' (or if that doesn't work on your system, try `conda install -c conda-forge cvxpy').



import numpy as np
import cvxpy as cp

def prob1():
    """Solve the following convex optimization problem:

    minimize        2x + y + 3z
    subject to      x  + 2y         <= 3
                         y   - 4z   <= 1
                    2x + 10y + 3z   >= 12
                    x               >= 0
                          y         >= 0
                                z   >= 0

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    x = cp.Variable(3, nonneg = True)
    c = np.array([2, 1, 3])
    objective = cp.Minimize (c.T @ x)

    A = np.array([[1, 2, 0], [0, 1, -4], [-2, -10, -3]])
    b = np.array([3, 1, -12])
    constraints = [A @x <= b]
    problem = cp.Problem(objective, constraints)
    s = problem.solve()
    return (x.value, s)


# Problem 2
def l1Min(A, b):
    """Calculate the solution to the optimization problem

        minimize    ||x||_1
        subject to  Ax = b

    Parameters:
        A ((m,n) ndarray)
        b ((m, ) ndarray)

    Returns:
        The optimizer x (ndarray)
        The optimal value (float)
    """
    
    assert A.shape[0] == b.shape[0], "mismatched dimensions"
    
    n = A.shape[1]
    #x = cp.Variable(n, nonneg = True)
    x = cp.Variable(n)
    objective = cp.Minimize(cp.norm(x, 1))
    constraints = [A @ x == b]
    
    problem = cp.Problem(objective, constraints)
    s = problem.solve()
    return (x.value, s)


# Problem 3
def prob3():
    """Solve the transportation problem by converting the last equality constraint
    into inequality constraints.

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    #p_1 + p_2 <= 7
    #p_3 + p_4 <= 2
    #p_5 + p_6 <= 4

    #p_1 + p_3 + p_5 = 5
    #p_2 + p_4 + p_6 = 8
    
    x = cp.Variable(6, nonneg = True)

    A = np.array([[1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1]])
    a = np.array([5, 8])

    B = np.array([[1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0], 
                  [0, 0, 0, 0, 1, 1]])
    b = np.array([7, 2, 4])

    constraints = [A @ x == a, B @ x <= b]

    c = np.array([4, 7, 6, 8, 8, 9])
    objective = cp.Minimize(c.T @ x)
    
    problem = cp.Problem(objective, constraints)
    s = problem.solve()
    return (x.value, s)


# Problem 4
def prob4():
    """Find the minimizer and minimum of

    g(x,y,z) = (3/2)x^2 + 2xy + xz + 2y^2 + 2yz + (3/2)z^2 + 3x + z

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
   #.5 (3x1^2 + x1x2 + x1x3 + x2^2 + x2x3 + 3x3^2 )
    Q = np.array([[3, 2, 1],[2, 4, 2],[1, 2, 3]])
    #3x1 + x3
    r = np.array([3, 0, 1])
    x = cp.Variable(3)

    problem = cp.Problem(cp.Minimize(.5 * cp.quad_form(x, Q) + r.T @ x))

    s = problem.solve()
    return (x.value, s)

# Problem 5
def prob5(A, b):
    """Calculate the solution to the optimization problem
        minimize    ||Ax - b||_2
        subject to  ||x||_1 == 1
                    x >= 0
    Parameters:
        A ((m,n), ndarray)
        b ((m,), ndarray)
        
    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    #.minimize ||Ax - b||_2
    # ||x||1 = 1
    #x nonneg

    n = A.shape[1]
    C = np.ones((n))
    one = np.ones((1))
    x = cp.Variable(n, nonneg = True)


    constraints = [C @ x == one]
    objective = cp.Minimize(cp.norm(A@x - b, 2))
    problem = cp.Problem(objective, constraints)
    s = problem.solve()
    return (x.value, s)


#optional
# Problem 6
def prob6():
    """Solve the college student food problem. Read the data in the file 
    food.npy to create a convex optimization problem. The first column is 
    the price, second is the number of servings, and the rest contain
    nutritional information. Use cvxpy to find the minimizer and primal 
    objective.
    
    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """	 
    raise NotImplementedError("Problem 6 Incomplete")
