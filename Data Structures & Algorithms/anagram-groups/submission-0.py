class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        retval = []
        temp_dict = {}
        ana_dict = {}
        if not strs:
            retval = strs
        else:
            for word in strs:
                for let in word:
                    if let in temp_dict:
                        temp_dict[let] += 1
                    else:
                        temp_dict[let] = 1
                key = tuple(sorted(temp_dict.items()))
                if key in ana_dict:
                    ana_dict[key].append(word)
                else:
                    ana_dict[key] = []
                    ana_dict[key].append(word)
                temp_dict = {}
            for value in ana_dict.values():
                retval.append(value)
        return retval
        