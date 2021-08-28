"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
"""


def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    num_search = 0
    zero_pointer = 0

    while num_search < len(nums):
        if nums[num_search] != 0 and nums[zero_pointer] == 0:
            nums[zero_pointer], nums[num_search] = nums[num_search], nums[zero_pointer]

        if nums[zero_pointer] != 0:
            zero_pointer += 1

        num_search += 1
