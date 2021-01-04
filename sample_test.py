
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
    a, b = 0, 1
    while True:     # Infinate loop
        yield a  # report value a during the pass
        a, b = b, a+b  # report next values


def is_multiple(n, m):
    """
    Write a short Python function,ismultiple(n, m),
    that takes two integervalues and returns True if
    n is a multiple of m,that is, n=mi for some integer i,
    and False otherwise.
    """
    if n % m == 0:
        return True
    return False


def is_even(k):
    """
    Write a short Python function, is even(k), that takes an integer value and
    returns True if k is even, and False otherwise. However, your function
    cannot use the multiplication, modulo, or division operators.
    """
    if not isinstance(k, (int, float)):
        raise TypeError('elements must be numeric')

    k_str = str(k)
    len_k = len(k_str)
    number = [i.isdigit() for i in k_str]
    if number:
        if int(k_str[len_k-1]) in range(0, 9, 2):
            return True
        else:
            return False


def minmax(data):
    """
    Write a short Python function, minmax(data), that takes a sequence of
    one or more numbers, and returns the smallest and largest numbers, in the
    form of a tuple of length two. Do not use the built-in functions min or
    max in implementing your solution.
    """
    def find_min_max(data):
        min_, max_ = data[0], data[1]
        for i in data:
            if (max_ < i):
                max_ = i
        for i in data:
            if (min_ > i):
                min_ = i
        return (min_, max_)

    if isinstance(data, List):
        return find_min_max(data)
    if isinstance(data, tuple):
        return find_min_max(data)
    if isinstance(data, set):
        temp_data = list(data)
        return find_min_max(temp_data)


def sum_squares(n):
    sum_ = []
    if n > 0:
        for i in range(n):
            sum_.append(i*i)
    return sum(sum_)


def sum_squares_(n):
    sum_ = sum([i*i for i in range(n) if i > 0])
    return sum_


def find_max(data):
    """ Return the max elements from a nonempty Python list.
    This function is classic example of an algo with a running time
    that grows proportional to n, as the loop executes for each pass
    """
    highest = data[0]
    for val in data:
        if val > highest:
            highest = val
    return highest

# if __name__ == "__main__":
#    arr = [1, 2, 4, 10, 5, 8]
#    # call function
#    if binary_search(arr, 4) == 2:
#        print("Passed Test")
#    else:
#        print("Failed Test")
