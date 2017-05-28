"""
P25 (*) Generate a random permutation of the elements of a list.
    Example:
    * (rnd-permu '(a b c d e f))
    (B A D C E F)
"""
import random


def rnd_permu(l):
    return random.sample(l, len(l))

l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k"]
print rnd_permu(l)
