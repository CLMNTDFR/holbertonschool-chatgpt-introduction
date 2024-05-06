#!/usr/bin/python3
import sys


def factorial(n):
    """
    Calculate the factorial of a given number recursively.

    Parameters:
    n (int): The number for which to compute the factorial.

    Returns:
    int: The factorial of the number 'n'.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Accept a number from command line arguments, calculate its factorial, and print it
f = factorial(int(sys.argv[1]))
print(f)
