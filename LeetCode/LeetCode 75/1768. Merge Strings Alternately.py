def mergeAlternately(word1: str, word2: str) -> str:
    merged = ""
    count = 0
    len1 = len(word1)
    len2 = len(word2)

    if len1 < len2:
        while count < len1:
            merged += word1[count] + word2[count]
            count += 1
        for i in range(count, len2):
            merged += word2[i]
    elif len1 > len2:
        while count < len2:
            merged += word1[count] + word2[count]
            count += 1
        for i in range(count, len1):
            merged += word1[i]
    else:
        while count < len1:
            merged += word1[count] + word2[count]
            count += 1

    return merged


class Solution(object):
    word1 = input("Enter word1: ")
    word2 = input("Enter word2: ")
    print(mergeAlternately(word1, word2))