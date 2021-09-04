"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.
"""


def checkInclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    letters_s1 = dict()
    for letter in s1:
        letters_s1[letter] = letters_s1.get(letter, 0) + 1

    for i in range(len(s2) - len(s1) + 1):
        substr = s2[i:i + len(s1)]

        for letter in letters_s1:
            if letters_s1[letter] != substr.count(letter):
                break
        else:
            return True
    return False
