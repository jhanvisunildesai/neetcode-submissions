class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        retval = 0
        temp = []
        for j in range(len(nums)):
            if i == j and nums[j] not in temp:
                temp.append(nums[j])
                i+=1
            else:
                if i != j and nums[j] not in temp:
                    nums[i] = nums[j]
                    temp.append(nums[j])
                    i+=1
            retval = len(temp)
        return retval 
        