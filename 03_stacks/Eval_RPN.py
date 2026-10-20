# Problem: Evaluate Reverse Polish Notation (NeetCode 17) 
# Category: Stack 
# Time Complexity: O(N) - Single pass through tokens list of length N 
# Space Complexity: O(N) - Worst-case stack space storing numerical operands

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "*/+-":
                stack.append(int(token))
            elif token == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b + a))
            elif token == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b * a))
            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b - a))
            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            else:
                continue
        return stack[0]
