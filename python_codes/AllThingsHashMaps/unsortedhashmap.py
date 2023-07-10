"""using MapBase class to implement a concrete Map ADT
- Relys on stroign key-value pairs in arbitrary order within a python list.

1. Initialize an empty table as self._table within the constructor
2. When a new key is entered into the map vira __setitem__(), 
we create a new instance of the nested _Item class, inherited from the MapBase.

3. Simple, but not efficient.
Its fundamental blocks __getitem__, __setitem__, and __delitem__
rely on a for loop to scan the underlying list of items in search of a 
matching key.
Best Case: a match found near the beginning of the list.
Worst Case: Entire list is exampined hence method runs in O(n) time on a map with n items.
 """

import MapBase from mapbase

class UnsortedTableMap(MapBase):
    """Map implementation using an unorder list.""" 
    def __init__(self):
        """Creating an empty map"""
        self._table = []

    def __getitem__(self, k):
        """Return value associate with key k (raise KeyError if not found)"""
        for item in self._table:
            if k == item._value:
                return item._value
        raise KeyError('Key Error: ' + repr(k))
    
    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        for item in self._table:
            if k == item._key: # found match:
                item._value = v # reassign value
                return  # and quit
        # did not find a match for key
        self._table.append(self._Item(k, v))

    def __delitem__(self, k):
        """Remove an item associated with key k(raise KeyError if not found)"""
        for j in range(len(self._table)):
            if k == self._table[j]._key: # foudn a match
                self._table.pop(j) # remove the item
                return  # and quit
        raise KeyError('Key Error: ' + repr(k))
    
    def __len__(self):
        """Return number of items in the map"""
        return len(self._table)
    
    def __iter__(self):
        """Generate iteration of the map's keys."""
        for item in self._table:
            yield item._key