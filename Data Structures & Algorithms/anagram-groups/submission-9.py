class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans1 = {}
        ans = []
        temp = []
        for word in strs:
            for c in word:
                temp.append(c)
            temp.sort()
            temp1 = "".join(temp)
            ans1.setdefault(temp1, []).append(word)
            temp = []
            temp1 = ""
        for value in ans1.values():
            ans.append(value)
        return ans
        