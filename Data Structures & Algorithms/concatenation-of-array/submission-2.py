class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_len = len(nums) 
        retval = [0] * 2*nums_len

        for i in range(nums_len):
            retval[i] = nums[i] 
            retval[i+nums_len] = nums[i] 
        return retval
        