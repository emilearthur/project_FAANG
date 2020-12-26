class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        if isinstance(d, int):
            self._coords = [0] * d

        if isinstance(d, (list, tuple)):
            self._coords = [0] * len(d)
            for i in range(len(d)):
                self._coords[i] = d[i]

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

        if isinstance(other, (list, tuple)):
            if len(self) != len(other):
                raise ValueError('dimension must agree')
            result_ = Vector(len(other))
            for j in range(len(self)):
                result_[j] = other[j]

            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j]*result_[j]
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

        if isinstance(other, (list, tuple)):
            if len(self) != len(other):
                raise ValueError('dimension must agree')
            result_ = Vector(len(other))
            for j in range(len(self)):
                result_[j] = other[j]

            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j]*result_[j]
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
            result[j] = -1*self[j]
        return result

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation


if __name__ == "__main__":
    # subtraction
    print("subtraction")
    r = Vector(5)
    r.__setitem__(2, 10)
    r.__setitem__(1, 16)
    r.__setitem__(3, 9)
    r.__setitem__(4, 15)
    print(r.__str__())
    print(r.__sub__([4, 1, 0, 8, 21]))
    print()

    # negative
    print("negative")
    r = Vector(5)
    r.__setitem__(2, 10)
    r.__setitem__(1, 16)
    r.__setitem__(3, 9)
    r.__setitem__(4, 15)
    print(r.__str__())
    print(r.__neg__())
    print()

    # addition
    print("addition")
    r = Vector(5)
    r.__setitem__(2, 10)
    r.__setitem__(1, 16)
    r.__setitem__(3, 9)
    r.__setitem__(4, 15)
    print(r.__str__())
    print(r.__add__([4, 1, 0, 8, 21]))

    s = Vector(5)
    s.__setitem__(4, 20)
    s.__setitem__(2, -4)
    s.__setitem__(1, -5)
    print(s.__str__())

    print(r.__add__(s))
    print()

    # multiplicative
    print("multiplicative")
    r = Vector(5)
    r.__setitem__(2, 10)
    r.__setitem__(1, 16)
    r.__setitem__(3, 9)
    r.__setitem__(4, 15)
    print(r.__str__())
    print(r.__mul__(3))
    print(r.__mul__(10))
    print()

    # multiplicative
    print("dot")
    r = Vector(5)
    r.__setitem__(2, 10)
    r.__setitem__(1, 16)
    r.__setitem__(3, 9)
    r.__setitem__(4, 15)
    print(r.__str__())
    s = Vector(5)
    s.__setitem__(4, 20)
    s.__setitem__(2, -4)
    s.__setitem__(1, -5)
    print(s.__str__())
    print(r.__mul__(s))
    p = [4, 1, 7, 2, 8]
    print(p)
    print(r.__mul__(p))
