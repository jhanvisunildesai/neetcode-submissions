import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {"+", "-", "*", "/"}
        retval = 0

        for s in tokens:
            if s in operands:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if s == "+":
                    ans = num1 + num2
                    stack.append(ans)
                if s == "-":
                    ans = num1 - num2
                    stack.append(ans)
                if s == "*":
                    ans = num1 * num2
                    stack.append(ans)
                if s == "/":
                    if num1/num2 <= 0:
                        ans = math.ceil(num1/num2)
                    else:
                        ans = math.floor(num1/num2)
                    stack.append(ans)
            else:
                stack.append(int(s))
        retval = stack.pop()
        return retval
        