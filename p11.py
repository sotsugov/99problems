"""
(*) Modified run-length encoding.
    Modify the result of problem P10 in such a way that if an element has no duplicates it is simply copied into the result list. Only elements with duplicates are transferred as (N E) lists.

    Example:
    * (encode-modified '(a a a a b c c a a d e e e e))
    ((4 A) B (2 C) (2 A) D (4 E))
"""
from itertools import groupby


def encode_modified(l):
    def aux(lg):
        if len(lg) > 1:
            return [len(lg), lg[0]]
        else:
            return lg[0]
    return [aux(list(group)) for key, group in groupby(l)]

l = ["a", "a", "a", "a", "b", "c", "c", "a", "a", "d", "e", "e", "e", "e"]
print encode_modified(l)
