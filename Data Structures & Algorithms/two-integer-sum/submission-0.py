class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        retval = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    retval = [i, j]
                    break

        return retval



        