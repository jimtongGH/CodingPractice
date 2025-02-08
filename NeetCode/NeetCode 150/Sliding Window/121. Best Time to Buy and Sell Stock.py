from typing import List


def maxProfit(prices: List[int]) -> int:
    maxP = 0
    minBuy = prices[0]

    for sell in prices:
        maxP = max(maxP, sell - minBuy)
        minBuy = min(minBuy, sell)
    print(maxP)
    return maxP


class Solution(object):
    prices = list(map(int, input("Enter the numbers separated by space: ").split()))
    maxProfit(prices)