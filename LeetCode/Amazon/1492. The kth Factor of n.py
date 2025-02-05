def kthFactor( n: int, k: int) -> int:
    factors = []
    for i in range (1, n + 1):
        if n % i == 0:
            factors.append(i)
    if len(factors) < k:
        print(-1)
        return -1
    else:
        print(factors[k - 1])
        return factors[k - 1]


class Solution(object):
    kthFactor(4, 4)