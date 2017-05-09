"""
(**) Run-length encoding of a list (direct solution).
    Implement the so-called run-length encoding data compression method directly. I.e. don't explicitly create the sublists containing the duplicates, as in problem P09, but only count them. As in problem P11, simplify the result list by replacing the singleton lists (1 X) by X.

    Example:
    * (encode-direct '(a a a a b c c a a d e e e e))
    ((4 A) B (2 C) (2 A) D (4 E))
"""
from itertools import groupby


def encode_direct(l):
    def aux(k, g):
        l_len = len(list(g))
        if l_len > 1:
            return [l_len, k]
        else:
            return k
    return [aux(key, group) for key, group in groupby(l)]

l = ["a", "a", "a", "a", "b", "c", "c", "a", "a", "d", "e", "e", "e", "e"]
print encode_direct(l)
