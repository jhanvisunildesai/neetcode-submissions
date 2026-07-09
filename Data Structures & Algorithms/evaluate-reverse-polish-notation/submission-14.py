import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {"+", "-", "*", "/"}
        retval = 0

        for s in tokens:
            print(s)
            if s in operands:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if s == "+":
                    ans = num1 + num2
                    stack.append(ans)
                    print(num1, s, num2)
                if s == "-":
                    ans = num1 - num2
                    stack.append(ans)
                    print(num1, s, num2)
                if s == "*":
                    ans = num1 * num2
                    stack.append(ans)
                    print(num1, s, num2)
                if s == "/":
                    if num1/num2 <= 0:
                        ans = math.ceil(num1/num2)
                    else:
                        ans = math.floor(num1/num2)
                    # ans = num1/num2
                    stack.append(ans)
                    print(num1, s, num2, ans)
                print(stack)
            else:
                stack.append(int(s))
                print(stack)
        retval = stack.pop()
        return retval
        