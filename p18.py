"""
P18 (**) Extract a slice from a list.
    Given two indices, I and K, the slice is the list containing the
    elements between the I'th and K'th element of the original list
    (both limits included). Start counting the elements with 1.

    Example:
    * (slice '(a b c d e f g h i k) 3 7)
    (C D E F G)
"""


def lslice(l, i, k):
    return l[i-1:k]

l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k"]
print lslice(l, 3, 7)
