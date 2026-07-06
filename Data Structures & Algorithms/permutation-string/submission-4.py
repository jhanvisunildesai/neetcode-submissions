class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        retval = False
        temp_dict = {}
        s1_dict = {}
        s1_len = len(s1) -1
        s2_len = len(s2) -1

        for s in s1:
            if s not in s1_dict:
                s1_dict[s] = 1
            else:
                s1_dict[s] += 1
        
        for i in range(len(s2)+1):
            j = i + s1_len
            if j > s2_len:
                break
            else:
                for k in range(i, j + 1):
                    if s2[k] not in temp_dict:
                        temp_dict[s2[k]] = 1
                    else:
                        temp_dict[s2[k]] += 1
            if temp_dict == s1_dict:
                retval = True
                break
            else:
                temp_dict = {}
        return retval