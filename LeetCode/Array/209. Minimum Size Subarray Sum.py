#First Method: Brute-force Approach
# TC: O(n^2), SC: O(1)
def minSubArrayLen1(target, nums) -> int:
    minLength = float('inf') # Initialize result to infinity
    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            if sum >= target:
                result = min(minLength, j - i + 1)
                break
    print(result)
    return result if result != float('inf') else 0

# Second Method: Sliding Window Approach

class Solution(object):
    nums = list[int](map(int, input("Enter numbers separated by spaces for nums: ").split()))
    target = int(input("Enter the target value: "))

    minSubArrayLen1(target, nums)

    