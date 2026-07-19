class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        retval = 0
        i = 0
        temp = {}

        for j in range(len(s)):
            if s[j] in temp:
                temp[s[j]] += 1
            else:
                temp[s[j]] = 1

            # Window is invalid
            while (j - i + 1) - max(temp.values()) > k:
                if temp[s[i]] == 1:
                    del temp[s[i]]
                else:
                    temp[s[i]] -= 1
                i += 1

            # Window is valid here
            retval = max(retval, j - i + 1)

        return retval
        