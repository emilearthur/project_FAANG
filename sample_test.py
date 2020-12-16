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


if __name__ == "__main__":
    arr = [1, 2, 4, 10, 5, 8]
    # call function
    if binary_search(arr, 4) == 2:
        print("Passed Test")
    else:
        print("Failed Test")
