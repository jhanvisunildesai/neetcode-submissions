class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     retval = []
    #     index1 = 0
    #     index2 = 0
    #     j = len(numbers) - 1

    #     for i in range(j):
    #         ans = self.getindices(i, j, numbers, target, numbers[i])
    #         if ans[0] == 1:
    #             retval = [numbers[i], numbers[ans[1]]]
    #             break
    #     return retval
    
    # def getindices(self, k:int, j:int, numbers: List[int], target, i):
    #     mid = int((k+j)/2)
    #     print(k, j, mid)
    #     retval = [0,0]
    #     if(k<=j):
    #         if numbers[mid] == target - i:
    #             retval = [1, mid]
    #         else:
    #             if (target - i <= numbers[mid]):
    #                return self.getindices(k, mid, numbers, target, i)
    #             else:
    #                 return self.getindices(mid + 1, j, numbers, target, i)
    #     return retval

        retval = []
        i = 0
        len_num = len(numbers)

        for i in range(len_num - 1):
            for j in range(i, len_num):
                if numbers[i] + numbers[j] == target:
                    retval.append(i+1)
                    retval.append(j+1)
                    break
            if retval:
                break
        
        print(retval)
        return retval

        