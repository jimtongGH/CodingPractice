from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    # 1 2 3 4
    res = [1] * len(nums) # 1 1 1 1

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    print(res)
    return res

class Solution(object):
    nums = list(map(int, input("Enter the numbers separated by space: ").split()))
    productExceptSelf(nums)