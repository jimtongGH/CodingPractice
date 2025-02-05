def partitionString(s: str) -> int:
    count = 1
    seen = set()

    for char in s:
        if char in seen:
            count += 1
            seen.clear()
        seen.add(char)

    return count

class Solution(object):
    s = input("Enter a string: ")
    print(partitionString(s))