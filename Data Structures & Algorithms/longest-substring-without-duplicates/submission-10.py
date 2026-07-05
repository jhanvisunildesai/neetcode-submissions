class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        retval = 0
        count = 0
        i = 0
        temp_dict = {}

        for j in range(len(s)):
            if s[j] not in temp_dict:
                temp_dict[s[j]] = j
                count = j - i + 1
                print(temp_dict, count)
            else:
                i = temp_dict[s[j]] + 1
                temp_dict[s[j]] = j
                count = j-i +1
                for key in list(temp_dict):
                    if temp_dict[key] < i:
                        del(temp_dict[key])
                print(i, temp_dict, count)
                
            if retval < count:
                retval = count

        return retval