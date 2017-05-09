"""
P14 (*) Duplicate the elements of a list.
    Example:
    * (dupli '(a b c c d))
    (A A B B C C C C D D)
"""


def dupli(l):
    return [x for x in l for i in range(2)]

l = ["a", "b", "c", "c", "d"]
print dupli(l)
