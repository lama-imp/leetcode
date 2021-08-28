"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""


def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = [0 for n in range(len(nums))]
    i = 0
    j = -1
    pos = len(nums) - 1
    while pos >= 0:
        if abs(nums[i]) < abs(nums[j]):
            ans[pos] = nums[j] ** 2
            j -= 1
        else:
            ans[pos] = nums[i] ** 2
            i += 1
        pos -= 1

    return ans
