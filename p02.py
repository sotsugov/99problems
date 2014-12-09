"""
(*) Find the last but one box of a list.
    Example:
    * (my-but-last '(a b c d))
    (C D)
"""


def p02(l):
    return l[-2]


if __name__ == "__main__":
    print p02(['a', 'b', 'c', 'd'])
