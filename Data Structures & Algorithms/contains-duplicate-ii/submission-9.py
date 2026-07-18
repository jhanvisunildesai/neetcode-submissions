class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        retval = False
        i = 0
        temp = {}
        for j in range(i, min(len(nums),k+1)):
            if nums[j] in temp:
                temp[nums[j]] += 1
            else:
                temp[nums[j]] = 1
        print(temp)
        if any(value > 1 for value in temp.values()):
            retval = True
        else:
            for j in range(k+1, len(nums)):
                # print(temp)
                if temp[nums[i]] == 1:
                    del temp[nums[i]]
                else:
                    temp[nums[i]] -= 1
                i += 1
                if nums[j] in temp:
                    temp[nums[j]] += 1
                else:
                    temp[nums[j]] = 1
                if any(value > 1 for value in temp.values()):
                    retval = True
                    break
                
    #     i = 0
    #     j = min(k, len(nums)-1)
    #     for j in range(min(k, len(nums)-1), len(nums)):
    #         retval = self.containsduplicate(i, j, nums)
    #         if retval == True:
    #             break
    #         else:
    #             i+=1
    #     return retval
    
    # def containsduplicate(self, i:int, j:int, nums: List[int]) -> bool:
    #     retval = False
    #     temp = []
    #     for k in range(i, j+1):
    #         if nums[k] in temp:
    #             retval = True
    #             break
    #         else:
    #             temp.append(nums[k])
        return retval

