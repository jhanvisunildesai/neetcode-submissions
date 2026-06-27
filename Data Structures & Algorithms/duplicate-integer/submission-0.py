class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = {}
        retval = False
        for num in nums:
            if num not in temp:
                temp[num] = 1
            else:
                retval = True
        return retval
        