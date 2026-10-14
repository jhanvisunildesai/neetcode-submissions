class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        slist = {}
        tlist = {}
        ans = False
        for i in s:
            if i in slist:
                slist[i] += 1
            else:
                slist[i] = 1

        for j in t:
            if j in tlist:
                tlist[j] += 1
            else:
                tlist[j] = 1
        
        if tlist == slist:
            ans = True
        return ans
        