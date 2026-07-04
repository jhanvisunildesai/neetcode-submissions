class Solution:
    def isValid(self, s: str) -> bool:
        # Brack_dicts ={“(“: “)”, “[“:”]”,”{“:”}”}
        brack_dicts = {
             ")": "(",
             "}": "{",
             "]": "["
        }
        retval = True

        stack=[]
        for char in s:
            if char not in brack_dicts:
                stack.append(char)
            else: 
                if not stack or stack.pop() != brack_dicts[char]:
                    retval = False
        if stack:
            retval = False
        return retval