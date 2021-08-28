"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
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
