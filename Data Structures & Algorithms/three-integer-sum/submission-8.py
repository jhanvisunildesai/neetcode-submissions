class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        retval = []
        temp_arr = []
        nums.sort()

        for i in range(len(nums) - 2):
            target = 0 - nums[i]
            temp_arr = []
            j = i+1
            k = len(nums) - 1
            while j < k:
                temp_arr = []
                if nums[j] + nums[k] == target:
                    temp_arr.append(nums[i])
                    temp_arr.append(nums[j])
                    temp_arr.append(nums[k])
                    temp_arr = sorted(temp_arr)
                    
                    if temp_arr not in retval and temp_arr:
                        retval.append(temp_arr)
                    j+=1
                if nums[j] + nums[k] < target:
                    j +=1
                if nums[j] + nums[k] > target:
                    k -=1

        return retval