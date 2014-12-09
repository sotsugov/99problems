"""
(*) Find the last box of a list.
    Example:
    * (my-last '(a b c d))
    (D)
"""


def p01(l):
    return l[-1]


if __name__ == "__main__":
    print p01(['a', 'b', 'c', 'd'])
