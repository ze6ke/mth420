# python_intro.py
"""Python Essentials: Introduction to Python.
Zeke Wander
Mth420
4/4/25
"""


# Problem 1 (write code below)
if __name__ == "__main__":
    print("Hello, world!")
# Indent with four spaces (NOT a tab).

# Problem 2
def sphere_volume(r):
    """ Return the volume of the sphere of radius 'r'.
    Use 3.14159 for pi in your computation.
    """
    return 4/3 *3.14159 * r**3


# Problem 3
def isolate(a, b, c, d, e):
    """ Print the arguments separated by spaces, but print 5 spaces on either
    side of b.
    """
    print(a,b, c, sep="     ", end=" ")
    print(d,e, end=" ")


# Problem 4
def first_half(my_string):
    """ Return the first half of the string 'my_string'. Exclude the
    middle character if there are an odd number of characters.

    Examples:
        >>> first_half("python")
        'pyt'
        >>> first_half("ipython")
        'ipy'
    """
    return my_string[0:len(my_string)//2]

def backward(my_string):
    """ Return the reverse of the string 'my_string'.

    Examples:
        >>> backward("python")
        'nohtyp'
        >>> backward("ipython")
        'nohtypi'
    """
    return my_string[::-1]


# Problem 5
def list_ops():
    """ Define a list with the entries "bear", "ant", "cat", and "dog".
    Perform the following operations on the list:
        - Append "eagle".
        - Replace the entry at index 2 with "fox".
        - Remove (or pop) the entry at index 1.
        - Sort the list in reverse alphabetical order.
        - Replace "eagle" with "hawk".
        - Add the string "hunter" to the last entry in the list.
    Return the resulting list.

    Examples:
        >>> list_ops()
        ['fox', 'hawk', 'dog', 'bearhunter']
    """
    l = ["bear", "ant", "cat", "dog"]
    l.append("eagle")
    l[2] = "fox"
    l.pop(1)
    l.sort(reverse=True)
    l[l.index("eagle")]="hawk"
    l[-1] = l[-1]+"hunter"
    return l
    

# Problem 6
def pig_latin(word):
    """ Translate the string 'word' into Pig Latin, and return the new word.

    Examples:
        >>> pig_latin("apple")
        'applehay'
        >>> pig_latin("banana")
        'ananabay'
    """
    if word[0] in "aeiou":
        return word+"hay"
    else:
        return word[1:] + word[0] + "ay"


# Problem 7
def palindrome():
    """ Find and retun the largest panindromic number made from the product
    of two 3-digit numbers.
    """
    def is_palindromic(n):
        return str(n) == str(n)[::-1]
    
    largest_palindrome = 1
    for i in range(900, 1000):
        for j in range(900, 1000):
            if is_palindromic(i*j):
                largest_palindrome = i*j
    
    return largest_palindrome
    

# Problem 8
def alt_harmonic(n):
    """ Return the partial sum of the first n terms of the alternating
    harmonic series, which approximates ln(2).
    """
    return sum([(-1)**(i+1)/i for i in range(1, n+1)])
    
