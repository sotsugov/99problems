"""
P15 (**) Replicate the elements of a list a given number of times.
    Example:
    * (repli '(a b c) 3)
    (A A A B B B C C C)
"""


def repli(l, n):
    return [x for x in l for i in range(n)]

l = ["a", "b", "c", "c", "d"]
print repli(l, 3)
