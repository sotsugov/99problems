"""
P16 (**) Drop every N'th element from a list.
    Example:
    * (drop '(a b c d e f g h i k) 3)
    (A B D E G H K)
"""


def drop(l, n):
    return [j for i, j in enumerate(l) if (i+1) % n]

l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "k"]
print drop(l, 3)
