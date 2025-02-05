# First Method: Brute-force Approach
# TC: O(n^2), SC: O(1)
def removeElement1(nums, val) -> int:
    i, length = 0, len(nums)
    while i < length:
        if nums[i] == val:
            nums.pop(i)
            nums.append('_')
            for j in range(i+1, length):
                nums[j - 1] = nums[j]
            length -= 1
            i -= 1
        i += 1
    print(length,", ", nums)
    return length

# Second Method: Fast & Slow Pointer
# TC: O(n), SC: O(1)
def removeElement2(nums, val) -> int:
    fastPointer, slowPointer = 0, 0
    while fastPointer < len(nums):
        if nums[fastPointer] != val:
            nums[slowPointer] = nums[fastPointer]
            slowPointer += 1
        else:
            nums.pop(fastPointer)
            fastPointer -= 1
        fastPointer += 1

    print(len(nums), ", ", nums)
    return len(nums)


# Third Method:



class Solution(object):
    nums = list[int](map(int, input("Enter numbers separated by spaces for nums: ").split()))
    val = int(input("Enter the target value: "))

    #removeElement1(nums, val)
    removeElement2(nums, val)