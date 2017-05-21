"""
P20 (*) Remove the K'th element from a list.
    Example:
    * (remove-at '(a b c d) 2)
    (A C D)
"""


def remove_at(l, k):
    return l[:k-1] + l[k:]

l = ["a", "b", "c", "d"]
print remove_at(l, 2)
