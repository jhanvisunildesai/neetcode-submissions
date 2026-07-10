class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        retval = 0
        exnums = []
        nums.sort()
        i = 0
        for n in nums:
            if n == val:
                break
            else:
                i+=1
                retval += 1

        for j in range(i, len(nums)):
            if i == len(nums)-1:
                break 
            if nums[j] > val:
                nums[i] = nums[j]
                i += 1
                retval += 1
        return retval