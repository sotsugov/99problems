"""
(**) Eliminate consecutive duplicates of list elements.
    If a list contains repeated elements they should be replaced with a single copy of the element. The order of the elements should not be changed.

    Example:
    * (compress '(a a a a b c c a a d e e e e))
    (A B C A D E)
"""
from collections import OrderedDict


def eliminate_dupes(sequence):
    return list(OrderedDict.fromkeys(sequence.split()))


print eliminate_dupes('a a a a b c c a a d e e e e')
