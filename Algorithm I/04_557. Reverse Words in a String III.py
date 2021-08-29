"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
"""


def reverseString(s):
    s = list(s)
    l = 0
    r = len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return ''.join(s)


def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    lst = list(map(reverseString, s.split()))
    return ' '.join(lst)
