# numpy_intro.py
"""Python Essentials: Intro to NumPy.
<Zeke Wander>
<Mth420>
<5/2/25>
"""

import numpy as np


def prob1():
    """ Define the matrices A and B as arrays. Return the matrix product AB. """
    A=np.array([3, -1, 4, 1, 5, -9]).reshape(2,3)
    B=np.array([2, 6, -5, 3, 5, -8, 9, 7, 9, -3, -2, -3]).reshape(3, -1)
    
    return (A@B)
    #raise NotImplementedError("Problem 1 Incomplete")


def prob2():
    """ Define the matrix A as an array. Return the matrix -A^3 + 9A^2 - 15A. """
    A=np.array([3, 1, 4, 1, 5, 9, -5, 3, 1]).reshape(3, -1)
    
    return(-A @ A @ A + 9 * A @ A - 15 * A) #change from print to return after feedback
    #raise NotImplementedError("Problem 2 Incomplete")


def prob3():
    """ Define the matrices A and B as arrays using the functions presented in
    this section of the manual (not np.array()). Calculate the matrix product ABA,
    change its data type to np.int64, and return it.
    """
    A = np.triu(np.ones((7, 7), dtype=np.int64))
    #B = 6*A - np.ones((7,7), dtype=np.int64) #corrected after feedback
    B = (5 * np.ones((7, 7), dtype=np.int64) - 6 * A).transpose() 
    return ((A @ B @ A).astype(np.int64))
    #raise NotImplementedError("Problem 3 Incomplete")


def prob4(A):
    """ Make a copy of 'A' and use fancy indexing to set all negative entries of
    the copy to 0. Return the resulting array.

    Example:
        >>> A = np.array([-3,-1,3])
        >>> prob4(A)
        array([0, 0, 3])
    """
    B = np.copy(A)
    B[B < 0] = 0
    return (B)
    #raise NotImplementedError("Problem 4 Incomplete")


def prob5():
    """ Define the matrices A, B, and C as arrays. Use NumPy's stacking functions
    to create and return the block matrix:
                                | 0 A^T I |
                                | A  0  0 |
                                | B  0  C |
    where I is the 3x3 identity matrix and each 0 is a matrix of all zeros
    of the appropriate size.
    """
    
    A = (np.arange(6)).reshape(3, 2).transpose()
    B = 3 * np.tril(np.ones((3, 3), dtype=np.int64))
    C = np.diag(3 * [-2])

    row1 = np.hstack((np.zeros((3, 3)), A.transpose(), np.eye(3)))
    row2 = np.hstack((A, np.zeros((2, 5))))
    row3 = np.hstack((B, np.zeros((3, 2)), C))
    combined = np.vstack((row1, row2, row3))

    return (combined)
    #raise NotImplementedError("Problem 5 Incomplete")


def prob6(A):
    """ Divide each row of 'A' by the row sum and return the resulting array.
    Use array broadcasting and the axis argument instead of a loop.

    Example:
        >>> A = np.array([[1,1,0],[0,1,0],[1,1,1]])
        >>> prob6(A)
        array([[ 0.5       ,  0.5       ,  0.        ],
               [ 0.        ,  1.        ,  0.        ],
               [ 0.33333333,  0.33333333,  0.33333333]])
    """
    return (A / (A.sum(axis=1).reshape(-1, 1)))
    #raise NotImplementedError("Problem 6 Incomplete")


def prob7():
    """ Given the array stored in grid.npy, return the greatest product of four
    adjacent numbers in the same direction (up, down, left, right, or
    diagonally) in the grid. Use slicing, as specified in the manual.
    """
    grid = np.load("grid.npy")
    
    return (max(np.max(grid[:, :-3] * grid[:, 1:-2] * grid[:, 2:-1] * grid[:, 3:]),
        np.max(grid[:-3, ] * grid[1:-2, :] * grid[2:-1, :] * grid[3:, :]),
        np.max(grid[:-3, :-3] * grid[1:-2, 1:-2] * grid[2:-1, 2:-1] * grid[3:, 3:]),
        np.max(grid[:-3, 3:] * grid[1:-2, 2:-1] * grid[2:-1, 1:-2] * grid[3:, :-3])))
    #Print ("I'm not supposed to do this problem")
    #raise NotImplementedError("Problem 7 Incomplete")
