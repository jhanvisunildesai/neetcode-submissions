class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        # j = 0
        # counter = 0
        # retval = []
        # count = {}
        
        # for i in range(len(nums)):
        #     if nums[i] == nums[j]:
        #         counter += 1
        #         # if counter == k:
        #         #     retval.append(nums[j])
        #     else:
        #         count[counter].append(nums[j])
        #         counter = 1
        #         j = i

        # print(max(count))
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        retval = list(sorted(count, key=count.get, reverse=True))[:k]
        print(count)
        return retval