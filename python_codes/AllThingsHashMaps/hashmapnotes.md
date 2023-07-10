'''
Five behavious highlighted,
- ability to query, 
- ability to add,
- ability to modify,
- ability to delete a key-value pair
- ability to report all such pairs

-------
Case Study
- counting words in a book
freq[word] = 1 + freq.get(word, 0)
// use the get method on the right hand side because
the current word might not exist in the dictionary;
the default value of 0 is appropriate in such a case.


freq = {}
for piece in open(filename).read().lower().split():
    # only consider alphabetic chars within this piece
    word = ''.join(c for c in piece if c.isalpha())
    if word: # require atleas one alphabetice character
        freq[word] = 1 + freq.get(word, 0)

max_word = ''
max_count = 0
for (w, c) in freq.items(): # (k, v) tuples represent (word, count)
    if c > max_count:
        max_word = w
        max_count = c
print("Most frequent word is ", max_word)
print("Its number of occurences is ", max_count)

abstract base class (abc in collections module):
Methods that are declared to be abstract in such a base
class must eb implemented by concrete sub-classes. However, 
an abstract base class may provide concrete implementation of 
other methods that depend upon use of the preseumend abstract methods.
Example of the TEMPLATE METHOD DESIGN PATTERN.


The module provideds two abstract base classes: 
1. Mapping
- Includes all nonmutation methods supported by python dict's class.
2. MutatbleMapping classes
- Extends the dict class to include mutable methods

Significance of these abstract ase classes is that they provide a framework to assist in creatign a user-defined map class 
The MutableMapping class provides concrete implementation for all behaviours other than the 
a): __getitem__()
b): __setitem__()
c): __delitem__()
d): __len__()
e): __iter__()

As we implement the map abstraction with various data structures, as long as we provide the five core behaviours, we can inherit all other derived behaviours by simply declaring MutableMapping as a parent class. 

The `__contains__` method, supporting the syntax k in M, could be implemented by making a guarded attempt to retrieve self[k] to determin if the key exists.

```python
def __contains__(self, k):
    try:
        self[k] # access via __getitem__
        return True
    except KeyError:
        return False # Attempt failed
```

A similar approach -- provide the logic of the setdefault method.
```python
def setdefault(self, k, d):
    try:
        return self[k] # if __getitem__ succeeds, return value
    except KeyError: 
        self[k] = d # set default value with __setitem__
        return d # and return that newly assigned value
```

In interest of code Re-use, the MapBase class, which is a subclass of the MutableMapping class is defined.
MapBase provides support for the composition design pattern. - Introduced when implementing a PQ in order to group a key-value pair as a single instance for internal use.

Equality is necessary for all our map implementation as a way to determine whether a key given as a pramete is equivalent to one that is already stored in the map. 
'''