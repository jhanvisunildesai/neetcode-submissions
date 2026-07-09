class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        retval = []
        temp_arr = []
        nums.sort()
        # print(nums)

        for i in range(len(nums) - 2):
            target = 0 - nums[i]
            temp_arr = []
            j = i+1
            k = len(nums) - 1
            while j < k:
                # print(i, j, k, target)
                temp_arr = []
                if nums[j] + nums[k] == target:
                    # print(nums[i], nums[j], nums[k])
                    temp_arr.append(nums[i])
                    temp_arr.append(nums[j])
                    temp_arr.append(nums[k])
                    temp_arr = sorted(temp_arr)
                    
                    if temp_arr not in retval and temp_arr:
                        retval.append(temp_arr)
                        # print( retval)
                    j+=1
                if nums[j] + nums[k] < target:
                    j +=1
                if nums[j] + nums[k] > target:
                    k -=1

        return retval
        # for i in range(len(nums) - 2):
        #     for j in range(i + 1, len(nums) - 1):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 temp_arr.append(nums[i])
        #                 temp_arr.append(nums[j])
        #                 temp_arr.append(nums[k])
        #                 temp_arr = sorted(temp_arr)
        #             # print(temp_arr)
        #             if temp_arr not in retval and temp_arr:
        #                 retval.append(temp_arr)
        #             temp_arr = []
        # return retval

        