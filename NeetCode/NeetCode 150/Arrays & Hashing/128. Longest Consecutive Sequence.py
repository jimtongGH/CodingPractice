from typing import List


def longestConsecutive(nums: List[int]) -> int:
    numSet = set(nums)
    longest = 0

    for num in numSet:
        if (num - 1) not in numSet:
            length = 1
            while num + length in numSet:
                length += 1
            longest = max(length, longest)
    print(longest)
    return longest

class Solution(object):
    nums = list(map(int, input("Enter the numbers separated by space: ").split()))
    longestConsecutive(nums)