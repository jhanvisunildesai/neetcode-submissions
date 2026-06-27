class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp1 = {}
        temp2 = {}
        for char in s:
            if char not in temp1:
                temp1[char] = 1
            else:
                temp1[char] += 1

        for char in t:
            if char not in temp2:
                temp2[char] = 1
            else:
                temp2[char] += 1

        retval = True if temp1 == temp2 else False
        print(retval)

        return retval

        