def gcdOfStrings(str1: str, str2: str) -> str:
    gcdStr = ""
    len1 = len(str1)
    len2 = len(str2)

    gcdStr1 = str1 + str2
    gcdStr2 = str2 + str1
    if gcdStr1 == gcdStr2:
        if len1 <= len2:
            for i in range(0, len1):
                for j in range(1, len1):
                    if str1[i] != str1[j]:
                        gcdStr += str1[i]
            return str1
        else:
            return str2
    else:
        return ""


class Solution(object):
    str1 = input("Enter str1: ")
    str2 = input("Enter str2: ")
    print(gcdOfStrings(str1, str2))