"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
"""


def rotate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    temp = nums[-k:]
    j = k
    for i in range(len(nums) - 1, k - 1, -1):
        nums[i] = nums[j]
        j -= 1
    for i in range(k):
        nums[i] = temp[i]

nums = [-1,-100,3,99]
rotate(nums, 2)
print(nums)