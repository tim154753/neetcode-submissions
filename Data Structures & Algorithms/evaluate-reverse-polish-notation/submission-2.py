
from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for char in tokens:
            if char in "+-/*":
                if char == "+":
                    res = stack.pop() + stack.pop()
                elif char == "-":
                    res = -1*stack.pop() + stack.pop()
                elif char == "*":
                    res = stack.pop() * stack.pop()
                elif char == "/":
                    res = int(1/stack.pop() * stack.pop())
                stack.append(res)
            else:
                stack.append(int(char))
        return stack[0]
