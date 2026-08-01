import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = re.sub(r'[^A-Za-z0-9]', '', s)
        s = s.lower()
        j = len(s) - 1
        retval = True
        for i in range(len(s)):
            if j == i:
                break
            else:
                if s[i] != s[j]:
                    retval = False
                    break
                else:
                    j -= 1
        
        return retval

        