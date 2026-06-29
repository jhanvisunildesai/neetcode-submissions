class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        retval = 0
        if nums:
            counter = 1
            nums = list(set(nums))
            nums.sort()
            print(nums)
            for n in range(1, len(nums)):
                # print(n)
                # print(nums[n-1], nums[n]-1)
                if nums[n-1] == (nums[n]-1):
                    counter += 1
                    # print(counter)
                else:
                    if counter > retval:
                        retval = counter
                    counter = 1
            if counter > retval:
                retval = counter
        return retval
        