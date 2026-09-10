class MinStack:

    def __init__(self):
        self.stack = []
        self.minVal = collections.deque()
    def push(self, val: int) -> None:
        if not self.minVal or val <= self.minVal[-1]:
            self.minVal.append(val)
        self.stack.append(val)
        return

    def pop(self) -> None:
        a = self.stack[-1]
        if a == self.minVal[-1]:
            self.minVal.pop()
        self.stack = self.stack[0:-1]
        return a

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minVal[-1]
        
