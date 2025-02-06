from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    indices = {}

    for i, n in enumerate(nums):
        indices[n] = i

    for i, n in enumerate(nums):
        diff = target - n
        if diff in indices and indices[diff] != i:
            print(i, indices[diff])
            return [i, indices[diff]]

class Solution(object):
    nums = list(map(int, input("Enter the numbers separated by space: ").split()))
    target = int(input("Enter the target sum: "))
    twoSum(nums, target)