# lstsq_eigs.py
"""Volume 1: Least Squares and Computing Eigenvalues.
Zeke Wander
MTH420
5/2/25
"""

import numpy as np
from cmath import sqrt
from scipy import linalg as la
from matplotlib import pyplot as plt


# Problem 1
def least_squares(A, b):
    """Calculate the least squares solutions to Ax = b by using the QR
    decomposition.

    Parameters:
        A ((m,n) ndarray): A matrix of rank n <= m.
        b ((m, ) ndarray): A vector of length m.

    Returns:
        x ((n, ) ndarray): The solution to the normal equations.
    """
    (Q,R) = la.qr(A, mode = "economic")
    
    x = np.linalg.inv(R) @ Q.transpose() @ b
    
    return(x)
    #raise NotImplementedError("Problem 1 Incomplete")

# Problem 2
def line_fit():
    """Find the least squares line that relates the year to the housing price
    index for the data in housing.npy. Plot both the data points and the least
    squares line.
    """
    yearstart = 2000
    
    data = np.load("housing.npy")

    b = prices = data[:, 1] #0-indexed year
    years = data[:, 0]
    A = np.hstack((np.ones((len(prices),1)), years.reshape(-1,1)))
    (x1,x2) = least_squares(A,b)
    fitline_x = np.linspace(np.min(years), np.max(years), 2)
    fitline_y = fitline_x * x2 + x1

    plt.plot(years + yearstart, prices, "o")
    plt.plot(fitline_x + yearstart, fitline_y)
    plt.show()


# Problem 3
def polynomial_fit():
    """Find the least squares polynomials of degree 3, 6, 9, and 12 that relate
    the year to the housing price index for the data in housing.npy. Plot both
    the data points and the least squares polynomials in individual subplots.
    """
    data = np.load("housing.npy")
    yearstart = 2000
    b = prices = data[:, 1] #0-indexed year
    years = data[:, 0].reshape(-1,1)
    for i in range(1, 5, 1):
        A = np.hstack((np.ones((len(prices),1)), years **range(1,(3 * i) + 1)))
        x = least_squares(A,b)
        fitline_y = (A * x).sum(axis = 1)

        plt.subplot(2, 2, i)
        plt.plot(years + yearstart, prices, "o")
        plt.plot(A[:,1] + 2000, fitline_y)
        plt.title(f"Degree {3 * i}")
    plt.tight_layout()
    plt.show()


#instructions say to stop after problem 3
def plot_ellipse(a, b, c, d, e):
    """Plot an ellipse of the form ax^2 + bx + cxy + dy + ey^2 = 1."""
    theta = np.linspace(0, 2*np.pi, 200)
    cos_t, sin_t = np.cos(theta), np.sin(theta)
    A = a*(cos_t**2) + c*cos_t*sin_t + e*(sin_t**2)
    B = b*cos_t + d*sin_t
    r = (-B + np.sqrt(B**2 + 4*A)) / (2*A)

    plt.plot(r*cos_t, r*sin_t)
    plt.gca().set_aspect("equal", "datalim")

    
# Problem 4
def ellipse_fit():
    """Calculate the parameters for the ellipse that best fits the data in
    ellipse.npy. Plot the original data points and the ellipse together, using
    plot_ellipse() to plot the ellipse.
    """
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def power_method(A, N=20, tol=1e-12):
    """Compute the dominant eigenvalue of A and a corresponding eigenvector
    via the power method.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The maximum number of iterations.
        tol (float): The stopping tolerance.

    Returns:
        (float): The dominant eigenvalue of A.
        ((n,) ndarray): An eigenvector corresponding to the dominant
            eigenvalue of A.
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def qr_algorithm(A, N=50, tol=1e-12):
    """Compute the eigenvalues of A via the QR algorithm.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The number of iterations to run the QR algorithm.
        tol (float): The threshold value for determining if a diagonal S_i
            block is 1x1 or 2x2.

    Returns:
        ((n,) ndarray): The eigenvalues of A.
    """
    raise NotImplementedError("Problem 6 Incomplete")
