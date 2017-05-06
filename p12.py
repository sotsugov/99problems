"""
(**) Decode a run-length encoded list.
    Given a run-length code list generated as specified in problem P11.
    Construct its uncompressed version.

"""
from p11 import encode_modified

def decode(l):
    def aux(g):
        if isinstance(g, list):
            return [(g[1], range(g[0]))]
        else:
            return [(g, [0])]
    return [x for g in l for x, R in aux(g) for i in R]

_l = ["a", "a", "a", "a", "b", "c", "c", "a", "a", "d", "e", "e", "e", "e"]
l = encode_modified(_l)
print decode(l)
