class SequenceIterator:
    """ An iterator for any Python's sequence types."""

    def __init__(self, sequence):
        """Create an iterator for the given sequence."""
        self._seq = sequence  # keep a reference to underlying data
        self._k = -1  # will increment to 0 on first call to next

    def __next__(self):
        """Returns the next element, or else raise StopIteration error."""
        self._k += 1
        if self._k < len(self._seq):
            return (self._seq[self._k])
        else:
            raise StopIteration()

    def __iter__(self):
        """By conversion, an iterator must return itself as an iterator."""
        return self