def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        print("False")
        return False

    count = [0] * 26
    for i in range(len(s)):
        # ord() function return Unicode (or ASCII) integer value of a single character
        # ord(s[i]) - ord('a') means position of letter eg. a - a = 0, b - a = 1
        # Using count to accord letter's frequency
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1

    for val in count:
        if val != 0:
            print("False")
            return False

    print("Ture")
    return True


class Solution(object):
    s = input("Enter the string s: ")
    t = input("Enter the string t: ")
    isAnagram(s, t)