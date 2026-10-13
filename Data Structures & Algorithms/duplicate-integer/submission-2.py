class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        ans = False
        for num in nums:
            if(num in freq):
                freq[num] += 1
            else:
                freq[num] = 1
        for value in freq.values():
            if value > 1:
                ans = True
                break;
        return ans
        