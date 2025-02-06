from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = {}

    # count frequency
    for num in nums:
        count[num] = 1 + count.get(num, 0)

    # create Bucket
    freq = [[] for i in range(len(nums) + 1)]

    # Bucket Sort
    for num, cnt in count.items():
        freq[cnt].append(num)

    # get the result
    result = []
    for num in freq[::-1]:
        if num:
            result.extend(num)
            if len(result) == k:
                print(result)
                return result
    # for i in range(len(freq) - 1, 0, -1):
    #     for num in freq[i]:
    #         result.append(num)
    #         if len(result) == k:
    #             return result

class Solution(object):
    nums = list(map(int, input("Enter the numbers separated by space: ").split()))
    k = int(input("Enter the number of elements: "))
    topKFrequent(nums, k)