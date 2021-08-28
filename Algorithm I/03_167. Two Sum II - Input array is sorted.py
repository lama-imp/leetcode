"""
Given an array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
"""


def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    l = 0
    r = len(numbers) - 1
    while l != r:
        sum_ = numbers[l] + numbers[r]
        if sum_ == target:
            return [l + 1, r + 1]
        elif sum_ > target:
            r -= 1
        else:
            l += 1
