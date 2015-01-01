"""
Print out dir(some_object) in an easier-to-scan format. Inspired by
http://github.com/inky/see/ but with a quite different notion of
what's easier to scan: we show it in columns like 'ls' does. See the
example below.

See http://github.com/inky/see/ for how to include this in your Python
startup.

## see(0)
#. __abs__            __hex__       __radd__        __rtruediv__      
#. __add__            __index__     __rand__        __rxor__          
#. __and__            __init__      __rdiv__        __setattr__       
#. __class__          __int__       __rdivmod__     __sizeof__        
#. __cmp__            __invert__    __reduce__      __str__           
#. __coerce__         __long__      __reduce_ex__   __sub__           
#. __delattr__        __lshift__    __repr__        __subclasshook__  
#. __div__            __mod__       __rfloordiv__   __truediv__       
#. __divmod__         __mul__       __rlshift__     __trunc__         
#. __doc__            __neg__       __rmod__        __xor__           
#. __float__          __new__       __rmul__        bit_length        
#. __floordiv__       __nonzero__   __ror__         conjugate         
#. __format__         __oct__       __rpow__        denominator       
#. __getattribute__   __or__        __rrshift__     imag              
#. __getnewargs__     __pos__       __rshift__      numerator         
#. __hash__           __pow__       __rsub__        real              

## columnize('hello worrrrrrrrld 1 2 3 4 5 6 7 8 9'.split())
#. hello          1   3   5   7   9  
#. worrrrrrrrld   2   4   6   8      

## columnize(['x'])
#. x  

## columnize([])
"""
__author__ = 'Darius Bacon'
__version__ = '0.1.0'
__copyright__ = 'Copyright (c) 2009 Darius Bacon'
__license__ = 'MIT X License'

import math

# (Maybe this should be called something other than see(), to avoid
# confusion? But view() is harder to type -- hmph.)
def see(x):
    "Show dir(x) in columns."
    columnize(dir(x))

def columnize(strings):
    "Given a sequence of strings, show them in columns."
    print_table(tabulate(strings))

def tabulate(strings, width=76):
    """Given a sequence of strings, return a matrix of the same
    strings in column order, trying to fit them in the given width."""
    maxwidth = max([1] + map(len, strings))
    ncols = max(1, min(len(strings), width // maxwidth))
    nrows = max(1, int(math.ceil(len(strings) / float(ncols))))
    t = [strings[i:i+nrows]
         for i in range(0, len(strings), nrows)]
    if t:
        t[-1] += [''] * (nrows * ncols - len(strings))
    return transpose(t)

def print_table(table, sep=' '):
    """Print a list of lists of strings as a table, so that columns
    line up nicely.  sep is the separator between columns."""
    # Adapted from print_table in utils.py in Peter Norvig's aima-python.
    sizes = [max(map(len, column)) for column in transpose(table)]
    for row in table:
        for size, string_ in zip(sizes, row):
            print string_.ljust(size), sep,
        print

def transpose(m):
    return zip(*m)
