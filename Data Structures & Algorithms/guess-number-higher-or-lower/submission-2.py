# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        retval = 0
        i = 1
        j = n
        pick = 0
        # hint = guess(pick)
        if guess(n) == 0:
            retval = n
        else:
            while (retval == 0):
                # if(guess(pick)==1):
                #     retval = pick    
                hint = guess(pick)
                if(hint == 0):
                    retval = pick 
                    break
                else:
                    if (hint == -1):
                        j = pick
                    else:
                        i = pick
                pick = int((i+j)/2)
                print(i, j, pick)
        return retval

        