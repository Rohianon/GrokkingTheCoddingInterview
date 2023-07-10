"""
Concrete implementation of a hashtable with separate chaining.
To represent a single bucket, we rely on an instance of the UnsortedTableMap class.

First 3 methods use index j to access the potential bucket in the bucket array, 
and check for the special case in which that table entry is None.
Only time we need a new bucket structure iw when _bucket_setitem is called on 
an otherwise empty slot. The remaining functionality relies on map behaviours
that are already suppoted by the individual UnsortedTableMap instances.

We need a bit of forethought to determine whether the application of __setitem__ on the 
chain causes a net increase in the size of the map. I.e.. whether the given key is new.
"""
from unsortedhashmap import UnsortedTableMap
from hashmapbase import HashMapBase
import doctest

class ChainHashMap(HashMapBase):
    """
    Hashmap implemented with separate chaining for collision resolution
    
    >>> chm = ChainHashMap()
    >>> chm['test_key'] = 'test_value'
    >>> chm['test_key']
    'test_value'
    >>> print("Test 1")
    Test 1
    >>> chm['test_key'] = 'new_value'
    >>> chm['test_key']
    'new_value'
    >>> del chm['test_key']
    >>> chm['test_key']
    Traceback (most recent call last):
    KeyError: "Key Error: 'test_key'"
    """

    def _bucket_getitem(self, j, k):
        """
        Get the item from the bucket at a specific index

        >>> print("Testing...")
        Testing...
        >>> chm = ChainHashMap()
        >>> chm['key'] = 'value'
        >>> chm._bucket_getitem(0, 'key')
        'value'
        """
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k)) # no match found
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        """
        Set the item in the bucket at a specific index.

        >>> chm = ChainHashMap()
        >>> chm._bucket_setitem(0, 'key', 'value')
        >>> chm['key']
        'value'
        """
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()  # bucket is new to the table
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:   # key was new to the table
            self._n += 1                    # increase overal map size

    def _bucket_delitem(self, j, k):
        """
        Delete the item in the bucket at a specific index.

        >>> chm = ChainHashMap()
        >>> chm['key'] = 'value'
        >>> chm._bucket_delitem(0, 'key')
        >>> chm['key']
        Traceback (most recent call last):
        KeyError: "Key Error: 'key'"
        """
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))     # no match found
        del bucket[k]                                   # may raise KeyError

    def __iter__(self):
        """
        Iterate over the keys in the hashmap.

        >>> chm = ChainHashMap()
        >>> chm['key1'] = 'value1'
        >>> chm['key2'] = 'value2'
        >>> chm['key3'] = 'value3'
        >>> keys = list(chm)
        >>> print(keys in ['key2', 'key1', 'key3'])
        True
        """
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key



if __name__ == "__main__":
    chm = ChainHashMap()
    chm['test_key'] = 'test_value'
    del chm['test_key']
    chm['key'] = 'value'
    del chm['key']
    chm['key1'] = 'value1'
    chm['key2'] = 'value2'
    chm['key3'] = 'value3'
    print(list(chm))
    # print(chm._bucket_getitem(0, 'key'))
    doctest.testmod()
