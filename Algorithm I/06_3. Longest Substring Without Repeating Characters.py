"""
Given a string s, find the length of the longest substring without repeating characters.
"""


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    ans = ''
    len_ans = 0
    for i in range(len(s)):
        ans = s[i]
        for j in range(i + 1, len(s)):
            if s[j] not in ans:
                ans += s[j]
            else:
                break
        if len(ans) > len_ans:
            len_ans = len(ans)
    return len_ans
