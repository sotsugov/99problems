"""
(*) Find out whether a list is a palindrome.
    A palindrome can be read forward or backward; e.g. (x a m a x).
"""


def is_palindrom(word):
    # Taking out white spaces to allow sentences
    word = ''.join(word.split())
    return True if word == word[::-1] else False

if __name__ == "__main__":
    print is_palindrom("stack cats")
    print is_palindrom("never odd or even")
    print is_palindrom("balance")
