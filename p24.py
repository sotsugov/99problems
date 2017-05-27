"""
P24 (*) Lotto: Draw N different random numbers from the set 1..M.
    The selected numbers shall be returned in a list.
    Example:
    * (lotto-select 6 49)
    (23 1 17 33 21 37)
"""
import random


def lotto_select(n, m):
    return random.sample(range(1, m + 1), n)

print lotto_select(6, 49)
