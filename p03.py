"""
(*) Find the K'th element of a list.
    The first element in the list is number 1.
    Example:
    * (element-at '(a b c d e) 3)
    C
"""


def p03(l, k):
    k -= 1
    return l[k]


if __name__ == "__main__":
    print p03(['a', 'b', 'c', 'd', 'e'], 3)
