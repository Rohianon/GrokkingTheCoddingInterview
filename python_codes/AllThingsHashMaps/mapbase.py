from typing import MutableMapping

"""
Extending the MutableMapping abstract class to provide
a non_public _Item class for use in our various map implementations
"""

class MapBase(MutableMapping):
    """
    Abstract base class that includes a nonpublic 
    _Item class.
    """
    # -----------------Nested _Item class ------------
    class _Item:
        """
        Lightweight composite to store key-value pairs as map items.
        """
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v
        
        def __eq__(self, other):
            return self._key == other._key # compare items based on their keys
        
        def __ne__(self, other):
            # opposite of __eq__
            return not (self == other) 
        
        def __lt__(self, other):
            # compare items based on their keys
            return self._key < other._key


