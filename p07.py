"""
(**) Flatten a nested list structure.
    Transform a list, possibly holding lists as elements into a 'flat' list
    by replacing each list with its elements (recursively).

    Example:
    * (my-flatten '(a (b (c d) e)))
    (A B C D E)

    Hint: Use the predefined functions list and append.
"""


def flatten(l):
    for i in l:
        if isinstance(i, list):
            for j in flatten(i):
                yield j
        else:
            yield i


if __name__ == "__main__":
    l = ['a', ['b', ['c', 'd'], 'e']]
    print list(flatten(l))
