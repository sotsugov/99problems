"""
P17 (*) Split a list into two parts; the length of the first part is given.
    Do not use any predefined predicates.

    Example:
    * (split '(a b c d e f g h i k) 3)
    ( (A B C) (D E F G H I K))
"""

def split(l, n):
    return l[:n], l[n:]


l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k"]
print split(l, 3)
