"""
P23 (**) Extract a given number of randomly selected elements from a list.
    The selected items shall be returned in a list.
    Example:
    * (rnd-select '(a b c d e f g h) 3)
    (E D A)
"""
import random


def rnd_select(l, k):
    return random.sample(l, k)

l = ["a", "b", "c", "d", "e", "f", "g", "h"]
print rnd_select(l, 3)
