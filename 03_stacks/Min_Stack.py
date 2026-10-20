# Problem: Min Stack (NeetCode 16) 
# Category: Stack / OOP Design 
# Time Complexity: O(1) for all operations (push, pop, top, getMin) 
# Space Complexity: O(N) auxiliary space for minimum state history tracking

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        current_min = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(current_min)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
