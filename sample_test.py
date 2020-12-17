# linear search function
from typing import List
from math import pi
from collections.abc import Iterable


def linear_search(arr: List, x: int) -> int:
    """
    Time complexity of O(n)
    """
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


def binary_search(arr: List, x: int):
    low = 0
    mid = 0
    high = len(arr)-1

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


def double_pi(x):
    if not isinstance(x, (int, float)):
        raise TypeError('x must be numeric')
    elif x < 0:
        raise ValueError('x cannot be negative')
    else:
        return x*pi


def sum(values):
    if not isinstance(values, Iterable):
        raise TypeError('pararmeter must be an Iterable type')

    total = 0
    for v in values:
        if not isinstance(v, (int, float)):
            raise TypeError('elements must be numeric')
        total += v
    return total


def factors(n):
    """
    Factor function without generator
    """
    results = []
    for k in range(1, n+1):
        if n % k == 0:
            results.append(k)
    # using comprehension syntax
    # results = [k fork in range(1, n+1) if n % k == 0]
    return results


def factors_gen(n):
    """
    Factors function using generator
    Notes: Its illegal to combine yield and return statement in the
    same implementation, other than a zero-argument return statement
    that causes a generator to end its execution.
    """
    for k in range(1, n+1):
        if n % k == 0:
            yield k


def factors_gen_(n):
    """
    Improving the efficiency of the generator byonly testing values up to the
    square root of that number, while reporting factor n/k that is associated
    with with each k (unless n//k equals k).
    Generator is different from one above as it does not generate in strictly
    increasing order
    """
    k = 1
    while k*k < n:  # while k < sqrt(n)
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k*k == n:  # special case if n is perfect square
        yield k


def fibonacci():
    a = 0
    b = 1
    while True:     # Infinate loop
        yield a  # report value a during the pass
        future = a + b
        a = b  # report next value
        b = future  # and this


if __name__ == "__main__":
    arr = [1, 2, 4, 10, 5, 8]
    # call function
    if binary_search(arr, 4) == 2:
        print("Passed Test")
    else:
        print("Failed Test")

"""
Other Notes:
list comprehension => [k for k in range(1, n+1)]
set comprehension => {k*k for k in range(1, n+1)}
generator comprehension => (k*k for k in range(1, n+1))
dictionary comprehension => {k: k*k for k in range(1, n+1)}
"""
