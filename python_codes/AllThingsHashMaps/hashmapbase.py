"""
Concrete implementation of a hashtable with separate chaining
"""

from random import randrange

from mapbase import MapBase


class HashMapBase(MapBase):
    """Abstract base class for map using hash-table with MAD compression"""

    def __init__(self, cap=11, p=109345121):
        """Create an empty hash-table map."""
        self._table = cap * [None]
        self._n = 0   # number of entries in the map
        self._prime = p   # prime for MAD compression
        self._scale = 1 + randrange(p-1)   # scale from 1 o p-1 for MAD
        self._shift = randrange(p)   # shift from 0 to p-1 for MAD

    def _hash_function(self, k):
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k) # may raise KeyError

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v) # subroutine maintaines self._n
        if self._n > len(self._table) // 2: # keep load factor <= 0.5
            self._resize(2 * len(self._table) -1)

    def __deleteitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k) # may raise KeyError
        self._n -= 1

    def _resize(self, c):  # resize the bucket to capacity c
        old = list(self.items())  # use iteration to record existing items
        self._table = c * [None]  # then reset the table to desired capacity
        self._n = 0     # n recomputed during subsequent adds
        for (k, v) in old:
            self[k] = v    # reinsert old key-value pair

    def _bucket_getitem(self, k, v):
        pass

    def _bucket_setitem(self, j, k, v):
        pass

    def _bucket_delitem(self, j, k):
        pass
