# First Method: Closed interval on both sides
# TC: O(log n), SC: O(1)
def search1(nums, target) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            print(mid)
            return mid
    else:
        print(-1)
        return -1

# Second Method: Left-closed, right-open interval
# TC: O(log n), SC: O(1)
def search2(nums, target) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            print(mid)
            return mid
    else:
        print(-1)
        return -1

class Solution(object):
    nums = list[int](map(int, input("Enter numbers separated by spaces for nums: ").split()))
    target = int(input("Enter the target value: "))

    # search1(nums, target)
    search2(nums, target)