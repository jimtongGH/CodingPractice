# First Method: Brute-force Approach, Use more time.
# TC: O(n) + O(n log n) = O(n log n) SC: O(n)
def sortedSquares1(nums) -> list[int]:
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    nums.sort()

    print(nums)
    return nums

# Second Method: Use a two-pointer approach, Use less time.
def sortedSquares2(nums) -> list[int]:
    left, right, resultPointer= 0, len(nums) - 1, len(nums) - 1
    result = [0] * len(nums)
    while left <= right:
        if nums[left] ** 2 < nums[right] ** 2:
            result[resultPointer] = nums[right] ** 2
            right -= 1
        else:
            result[resultPointer] = nums[left] ** 2
            left += 1
        resultPointer -= 1
    print(result)
    return result

class Solution(object):
    nums = list[int](map(int, input("Enter numbers separated by spaces for nums: ").split()))

    #sortedSquares1(nums)
    sortedSquares2(nums)