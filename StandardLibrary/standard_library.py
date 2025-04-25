# standard_library.py
"""Python Essentials: The Standard Library.
Zeke Wander
MTH420
4/18/25
"""

from math import sqrt


# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order, separated by a comma).
    """
    return (min(L),max(L),sum(L)/len(L))
    #raise NotImplementedError("Problem 1 Incomplete")


# Problem 2
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test integers, strings, lists, tuples, and sets. Print your results.
    """
    i = 1
    j=i
    j=2
    print (f"Integers are{'' if j==i else ' not'} mutable.")
    
    i="hi"
    j=i
    j+=" there"
    print (f"String are{'' if j==i else ' not'} mutable.")
    
    i=[1,2,3]
    j=i
    j[1]=2
    print (f"Lists are{'' if j==i else ' not'} mutable.")
    
    i=(1,2,3)
    j=i
    j=(1,2) #there are no modification calls.  This call would create a new item for a list as well.
    print (f"Tuples are{'' if j==i else ' not'} mutable.")
    
    i={1,2,3}
    j=i
    j.add(4)
    print (f"Sets are{'' if j==i else ' not'} mutable.")

    #raise NotImplementedError("Problem 2 Incomplete")


# Problem 3
def hypot(a, b):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any functions other than sum(), product() and sqrt() that are
    imported from your 'calculator' module.

    Parameters:
        a: the length one of the sides of the triangle.
        b: the length the other non-hypotenuse side of the triangle.
    Returns:
        The length of the triangle's hypotenuse.
    """
    #import calculator as c
    #return c.sqrt(c.sum(c.product(a,a), c.product(b,b)))
    import calculator
    return calculator.sqrt(calculator.sum(calculator.product(a,a), calculator.product(b,b)))
    #raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    from itertools import combinations, chain
    
    ps = [combinations(A,i) for i in range(len(A)+1)]
    return ([set(c) for c in chain(*ps)])
    #raise NotImplementedError("Problem 4 Incomplete")


# Problem 5: Implement shut the box.
def shut_the_box(player, timelimit):
    """Play a single game of shut the box."""
    raise NotImplementedError("Problem 5 Incomplete")
