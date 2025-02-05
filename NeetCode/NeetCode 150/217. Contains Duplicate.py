from typing import List

# def containsDuplicate1(nums: List[int]) -> bool:
#     flag = False
#     for i in range(0, len(nums)):
#         for j in range(i+1, len(nums)):
#             if nums[i] == nums[j]:
#                 print("true")
#                 flag = True
#                 return True
#
#     if not flag:
#         print("false")
#         return False

# Duplicate can use Hash Set to be checked

def containsDuplicate2(nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

class Solution(object):
    nums = list(input("Input list of integers:"))
    # containsDuplicate1(nums)
    containsDuplicate2(nums)