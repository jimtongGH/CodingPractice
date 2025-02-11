def lengthOfLongestSubstring(s: str) -> int:
    mp = {}
    l = 0
    res = 0

    for r in range(len(s)):
        if s[r] in mp:
            l = max(mp[s[r]] + 1, l)
        mp[s[r]] = r
        res = max(res, r - l + 1)
    print(res)
    return res


class Solution(object):
    s = input("Enter the string: ")
    lengthOfLongestSubstring(s)
