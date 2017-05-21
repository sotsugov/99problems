"""
P21 (*) Insert an element at a given position into a list.
    Example:
    * (insert-at 'alfa '(a b c d) 2)
    (A ALFA B C D)
"""


def insert_at(a, l, k):
    return l[:k-1] + [a] + l[k-1:]

l = ["a", "b", "c", "d"]
print insert_at('alfa', l, 2)
