class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
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

        