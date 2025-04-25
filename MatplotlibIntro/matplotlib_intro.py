# matplotlib_intro.py
"""Python Essentials: Intro to Matplotlib.
Zeke Wander
MTH420
4/25/25
"""

import numpy as np
from matplotlib import pyplot as plt

# Problem 1
def var_of_means(n):
    """ Create an (n x n) array of values randomly sampled from the standard
    normal distribution. Compute the mean of each row of the array. Return the
    variance of these means.

    Parameters:
        n (int): The number of rows and columns in the matrix.

    Returns:
        (float) The variance of the means of each row.
    """
    arr = np.random.normal(size=(n, n))
    means = np.mean(arr, axis=1)
    return (np.var(means))

def prob1():
    """ Create an array of the results of var_of_means() with inputs
    n = 100, 200, ..., 1000. Plot and show the resulting array.
    """
    
    arr = np.array([ var_of_means(n*100) for n in range(1,11)])
    plt.plot(arr)

# Problem 2
def prob2():
    """ Plot the functions sin(x), cos(x), and arctan(x) on the domain
    [-2pi, 2pi]. Make sure the domain is refined enough to produce a figure
    with good resolution.
    """
    x=np.linspace(-2*np.pi, 2*np.pi, 50)
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x))
    plt.plot(x, np.arctan(x))
    plt.show()


# Problem 3
def prob3():
    """ Plot the curve f(x) = 1/(x-1) on the domain [-2,6].
        1. Split the domain so that the curve looks discontinuous.
        2. Plot both curves with a thick, dashed magenta line.
        3. Set the range of the x-axis to [-2,6] and the range of the
           y-axis to [-6,6].
    """
    #left part of graph
    x1 = np.linspace(-2,.9,50)
    plt.plot(x1, 1/(x1-1), "m--", linewidth=4)

    #right part of graph
    x2 = np.linspace(1.1,6,50)
    plt.plot(x2, 1/(x2-1), "m--", linewidth=4)
    plt.xlim(-2,6)
    plt.ylim(-6,6)
    plt.show()


# Problem 4
def prob4():
    """ Plot the functions sin(x), sin(2x), 2sin(x), and 2sin(2x) on the
    domain [0, 2pi], each in a separate subplot of a single figure.
        1. Arrange the plots in a 2 x 2 grid of subplots.
        2. Set the limits of each subplot to [0, 2pi]x[-2, 2].
        3. Give each subplot an appropriate title.
        4. Give the overall figure a title.
        5. Use the following line colors and styles.
              sin(x): green solid line.
             sin(2x): red dashed line.
             2sin(x): blue dashed line.
            2sin(2x): magenta dotted line.
    """
    specs = [
    {'fn': lambda x: np.sin(x), 'style': "g", 'title': "sin(x)"}, 
     {'fn': lambda x: np.sin(2*x), 'style': "r--", 'title': "sin(2x)"}, 
     {'fn': lambda x: 2*np.sin(x), 'style': "b--", 'title': "2sin(x)"}, 
     {'fn': lambda x: 2*np.sin(2*x), 'style': "m:", 'title': "2sin(2x)"}
    ]
    
    x = np.linspace(0,2*np.pi, 50)
    
    for i in range(0, 4):
        axis = plt.subplot(2,2,i+1)
        axis.plot(x, specs[i]['fn'](x), specs[i]['style'])
        axis.set_title(specs[i]['title'])
        axis.axis([0, 2*np.pi, -2,2])

    plt.suptitle("some graphs")

    plt.show()


# Problem 5
def prob5():
    """ Visualize the data in FARS.npy. Use np.load() to load the data, then
    create a single figure with two subplots:
        1. A scatter plot of longitudes against latitudes. Because of the
            large number of data points, use black pixel markers (use "k,"
            as the third argument to plt.plot()). Label both axes.
        2. A histogram of the hours of the day, with one bin per hour.
            Label and set the limits of the x-axis.
    """
    data = np.load("FARS.npy")

    plt.figure(figsize=(6,8))

    #map
    plt.subplot(2,1,1)
    plt.plot(data[1:,1], data[1:,2], "k,")
    plt.axis("equal")
    plt.xlabel("longitude")
    plt.ylabel("latitude")

    #histogram
    plt.subplot(2,1,2)
    plt.hist(data[1:,0], bins=24, range=[0,24])
    plt.xlabel("hour")
    plt.ylabel("accidents")

    plt.show()


# Problem 6
def prob6():
    """ Plot the function g(x,y) = sin(x)sin(y)/xy on the domain
    [-2pi, 2pi]x[-2pi, 2pi].
        1. Create 2 subplots: one with a heat map of g, and one with a contour
            map of g. Choose an appropriate number of level curves, or specify
            the curves yourself.
        2. Set the limits of each subplot to [-2pi, 2pi]x[-2pi, 2pi].
        3. Choose a non-default color scheme.
        4. Include a color scale bar for each subplot.
    """
    x = np.linspace(-2*np.pi, 2*np.pi, 50)
    y = x.copy()

    X,Y = np.meshgrid(x,y)
    Z = np.sin(X) * np.sin(Y)/(X*Y)

    plt.subplot(1,2,1)
    plt.pcolormesh(X, Y, Z, cmap="coolwarm")
    plt.colorbar()
    plt.axis([-2*np.pi, 2*np.pi, -2*np.pi, 2*np.pi])

    plt.subplot(1,2,2)
    plt.contour(X, Y, Z, 12, cmap="coolwarm")
    plt.colorbar()
    plt.axis([-2*np.pi, 2*np.pi, -2*np.pi, 2*np.pi])

    plt.show()
