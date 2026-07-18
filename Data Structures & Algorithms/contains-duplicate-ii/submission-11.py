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
        return retval

