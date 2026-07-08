class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        retval = min(strs, key=len)
        i = 0

        for word in strs:
            for s in word:
                # print(retval, i)
                if not retval:
                    retval = ""
                    break
                if s != retval[i]:
                    retval = retval[:i]
                i += 1
                if i >= len(retval):
                    i = 0
                    break
        return retval
        