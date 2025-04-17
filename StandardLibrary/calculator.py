
from math import sqrt

def sum(x,y):
    """Sums x and y.
    
    Parameters:
        x,y: anything that can be *'d together.

    Returns:
        result of x*y
    """
    return(x+y)

def product(x,y):
    """Multiplies x and y.
    
    Parameters:
        x,y: anything that can be *'d together.

    Returns:
        result of x*y
    """
    return (x*y)

if __name__ == "__main__":
    print(f"sum(1,1) = {sum(1,1)}")
    print(f"product(1,1) = {product(1,1)}")
    print(f"sqrt(1) = {sqrt(1)}")