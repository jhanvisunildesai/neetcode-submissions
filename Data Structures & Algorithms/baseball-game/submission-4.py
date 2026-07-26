class Solution:
    def calPoints(self, operations: List[str]) -> int:
        retval = 0
        stack = []
        for op in operations:
            if op.isdigit() or (op.startswith("-") and op[1:].isdigit()):
                stack.append(int(op))
            if op == "+":
                stack.append(int(stack[-1]+stack[-2]))
            if op == "D":
                stack.append(int(stack[-1])*2)
            if op == "C":
                stack.pop()
        retval = sum(stack)
        return retval