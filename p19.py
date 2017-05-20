"""
P19 (**) Rotate a list N places to the left.
    Examples:
    * (rotate '(a b c d e f g h) 3)
    (D E F G H A B C)

    * (rotate '(a b c d e f g h) -2)
    (G H A B C D E F)
"""


def rotate(l, k):
    return l[k:] + l[:k]

l = ["a", "b", "c", "d", "e", "f", "g", "h"]
print rotate(l, 3)
print rotate(l, -2)
