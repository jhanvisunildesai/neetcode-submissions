class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        # remcount = 0
        retval = True

        # for i in range(int(j/2)
        while(i<j):
            # print(s[i], s[j], remcount)
            if s[i] == s[j]:
                i += 1 
                j -= 1
            else:
                if s[i] != s[j]:
                    #  and remcount == 0:
                    # remcount += 1
                    if self.ispalindrome( i, j-1, s) or self.ispalindrome(i+1, j, s):
                        retval = True
                    else: 
                        retval = False
                    break
                # else: 
                #     retval = False
                #     break       
    
        return retval

    def ispalindrome(self, i: int, j: int, s: str) -> bool:
        retval = True
        while(i<j):
            # print(s[i], s[j], remcount)
            if s[i] == s[j]:
                i += 1 
                j -= 1
            else:
                retval = False
                break
        return retval
