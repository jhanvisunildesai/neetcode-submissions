class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        retval = []
        i = 0
        for j in range(k-1, len(nums)):
            retval.append(max(nums[i:j+1]))
            # print(max(nums[i:j+1]), nums[i:j+1], j)
            i += 1
        return retval