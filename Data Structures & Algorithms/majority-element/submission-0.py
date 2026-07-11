class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        retval = 0
        maxcount = 0
        count = 0
        current = nums[0]
        print(nums)

        for n in nums:
            if n == current:
                count +=1
            else:
                if count > maxcount:
                    retval = current
                    maxcount = count
                current = n 
                count = 1
            print(count, current, maxcount, retval)
        if count > maxcount:
            retval = current
            maxcount = count
        return retval
        