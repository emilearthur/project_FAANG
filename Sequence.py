"""
collections.Sequence abstract base class defines the behaviors common
to Python's list, str and tuple classes, as sequences that support element
access via an integer index. Also, collections.Sequence class provides concrete
implementations of methods, count, index and __contains__ that can be inherited
by any class that provides concrete implementations of both __len__ and
__getitem__.
"""

from abc import ABCMeta, abstractmethod


class Sequence(metaclass=ABCMeta):
    """Our own  version of collections.Sequence abstract base class."""

    @abstractmethod
    def __len__(self):
        """Return the length of the sequence."""

    @abstractmethod
    def __getitem__(slef, j):
        """Return the element at index j of the sequence"""

    def __contains____(self, val):
        """Return True if val found in the sequence; False otherwise."""
        for j in range(len(self)):
            if self[j] == val:
                return True
            return False

    def index(self, val):
        """Return leftmost index at which val is found (or else raise ValueError).
        """
        for j in range(len(self)):
            if self[j] == val:      # leftmost match
                return j
            raise ValueError('value not in sequence')

    def count(self, val):
        """Return leftmost index at which val is found (or else raise ValueError).
        """
        k = 0
        for j in range(len(self)):
            if self[j] == val:
                k += 1
        return k
