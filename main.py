from datetime import datetime
import time


# Part 1
def clock(n):
    """
    Show the time and update it once for n seconds
    """
    for i in range(n):
        t = datetime.now()
        print(t.strftime("%X"), end="\r")
        time.sleep(1)
        

# Part 2
def lcm(a, b):
    """
    Returns the lowest common multiple of a and b
    a : int
    The first number
    b : int
    The second number
    """
    a1 , b1 = a, b
    while a != b:
        if a < b:
            a += a1
        else:
            b += b1
    return a
        


# Part 3
def gcf(a, b):
    """
    return the greatest common factor of a and b
    a : int
    The first number
    b : int
    The second number
    """
    while b != 0:
        r = a%b
        a = b
        b = r
    return a

