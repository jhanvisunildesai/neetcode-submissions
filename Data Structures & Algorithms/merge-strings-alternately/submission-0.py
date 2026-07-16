class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        retval = ""
        
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                retval = retval + word1[i]
            if i < len(word2):
                retval = retval + word2[i]

        return retval