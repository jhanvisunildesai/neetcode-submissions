class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = [0] * len(nums)
        retval = []

        for i in range(len(nums)):
            if i == 0:
                arr1.append(nums[i])
            else:
                arr1.append(nums[i] * arr1[i-1])
        
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                arr2[i] = nums[i]
            else:
                arr2[i] = nums[i] * arr2[i+1]

        for i in range(len(nums)):
            j = i-1
            k = i+1
            if j >= 0:
                num1 = arr1[j]
            else:
                num1 = 1
            if k < len(nums):
                num2 = arr2[k]
            else:
                num2 = 1
            retval.append(num1*num2)
        return retval

        