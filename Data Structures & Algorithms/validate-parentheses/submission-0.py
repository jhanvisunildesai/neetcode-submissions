class Solution:
    def isValid(self, s: str) -> bool:
        # Brack_dicts ={“(“: “)”, “[“:”]”,”{“:”}”}
        brack_dicts = {
             ")": "(",
             "}": "{",
             "]": "["
        }
        retval = True
        # print(brack_dicts)
        stack=[]
        for char in s:
            if char not in brack_dicts:
                stack.append(char)
            else: 
                if not stack or stack.pop() != brack_dicts[char]:
                    retval = False
                # if stack.pop != stack[char]:
                #     retval = False
        if stack:
            retval = False
        return retval