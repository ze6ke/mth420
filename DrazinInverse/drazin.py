# drazin.py
"""Volume 1: The Drazin Inverse.
Zeke Wander
MTH420
5/9/25
"""

import numpy as np
from scipy import linalg as la


def laplacian(A):
    """Compute the Laplacian matrix of the adjacency matrix A,
    as well as the second smallest eigenvalue.

    Parameters:
        A ((n,n) ndarray) adjacency matrix for an undirected weighted graph.

    Returns:
        L ((n,n) ndarray): the Laplacian matrix of A
    """
    D = A.sum(axis=1)    # The degree of each vertex (either axis).
    return np.diag(D) - A


# Helper function for problems 1 and 2.
def index(A, tol=1e-5):
    """Compute the index of the matrix A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.

    Returns:
        k (int): The index of A.
    """

    # test for non-singularity
    if not np.isclose(la.det(A), 0):
        return 0

    n = len(A)
    k = 1
    Ak = A.copy()
    while k <= n:
        r1 = np.linalg.matrix_rank(Ak)
        r2 = np.linalg.matrix_rank(np.dot(A,Ak))
        if r1 == r2:
            return k
        Ak = np.dot(A,Ak)
        k += 1

    return k


# Problem 1
def is_drazin(A, Ad, k):
    """Verify that a matrix Ad is the Drazin inverse of A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.
        Ad ((n,n) ndarray): A candidate for the Drazin inverse of A.
        k (int): The index of A.

    Returns:
        (bool) True of Ad is the Drazin inverse of A, False otherwise.
    """
    
    if not np.allclose(A@Ad, Ad@A): return(False)
    if not np.allclose(np.linalg.matrix_power(A, k+1) @ Ad, np.linalg.matrix_power(A, k)): return (False)
    if not np.allclose(Ad@A@Ad, Ad): return(False)
    
    return(True)


# Problem 2
def drazin_inverse(A, tol=1e-4):
    """Compute the Drazin inverse of A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.

    Returns:
       ((n,n) ndarray) The Drazin inverse of A.
    """
    (n,n)=np.shape(A)
    (T1, Q1, k1) = la.schur(A, sort=lambda x: abs(x) > tol)
    (T2, Q2, k2) = la.schur(A, sort=lambda x: abs(x) <= tol)
    U = np.hstack((Q1[:,:k1], Q2[:,:k2]))
    Uinv = la.inv(U)
    V = Uinv@A@U
    Z = np.zeros((n,n))
    if k1 >= 0:
        Z[:k1,:k1] = la.inv(V)[:k1,:k1]
    Dinv = U@Z@Uinv
    return (Dinv)


# Problem 3
def effective_resistance(A):
    """Compute the effective resistance for each node in a graph.

    Parameters:
        A ((n,n) ndarray): The adjacency matrix of an undirected graph.

    Returns:
        ((n,n) ndarray) The matrix where the ijth entry is the effective
        resistance from node i to node j.
    """
    (n,n) = np.shape(A)
    L = laplacian(A)
    eye = np.eye(n)
    r = np.zeros((n,n)) # create an empty array for the result
    for i in range(n): #process each row
        Lj = np.vstack((L[:i, :], eye[i,:], L[i+1:, :]))  #replace the ith row of the laplacian with the ith row of the identity matrix
        Ljd = drazin_inverse(Lj) #calculate the drazin inverse
        r[i,:] = np.diag(Ljd) # and save the diagonal as the effective resistance for row i
    r[np.eye(n, dtype=bool)] = 0 # override effective resistance for nodes to themselves to be 0
    return (r)
    
#Complete Lab 14: Drazin Inverse from Volume 1 Labs at https://foundations-of-applied-mathematics.github.io/Links to an external site. ,   except stop after Problem 3. (Note: see Lab 5 for description of Graph Laplacian). (Requires scipy).  



# Problems 4 and 5
class LinkPredictor:
    """Predict links between nodes of a network."""

    def __init__(self, filename='social_network.csv'):
        """Create the effective resistance matrix by constructing
        an adjacency matrix.

        Parameters:
            filename (str): The name of a file containing graph data.
        """
        raise NotImplementedError("Problem 4 Incomplete")


    def predict_link(self, node=None):
        """Predict the next link, either for the whole graph or for a
        particular node.

        Parameters:
            node (str): The name of a node in the network.

        Returns:
            node1, node2 (str): The names of the next nodes to be linked.
                Returned if node is None.
            node1 (str): The name of the next node to be linked to 'node'.
                Returned if node is not None.

        Raises:
            ValueError: If node is not in the graph.
        """
        raise NotImplementedError("Problem 5 Incomplete")


    def add_link(self, node1, node2):
        """Add a link to the graph between node 1 and node 2 by updating the
        adjacency matrix and the effective resistance matrix.

        Parameters:
            node1 (str): The name of a node in the network.
            node2 (str): The name of a node in the network.

        Raises:
            ValueError: If either node1 or node2 is not in the graph.
        """
        raise NotImplementedError("Problem 5 Incomplete")
