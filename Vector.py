from typing import List

class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        if isinstance(d, int):
            self._coords = [0] * d
        if isinstance(d, List):
            self._coords = [0] * d

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector"""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):
            raise ValueError('dimension must agree')
        result = Vector(len(self))  # start with vecotr of zero
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __sub__(self, other):
        """Return subtraction of two vectors."""
        if len(self) != len(other):
            raise ValueError('dimension must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __mul__(self, other):
        if isinstance(other, int):
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j]*other
            return result
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError('dimension must agree')
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j]*other[j]
            return sum(result)

    def __rmul__(self, other):
        if isinstance(other, int):
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j]*other
            return result
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError('dimension must agree')
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j]*other[j]
            return sum(result)

    def __eq__(self, other):
        """Return True if vector has same coordinate as other."""
        return self.__coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other

    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = 0 - self[j]
        return result

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation
