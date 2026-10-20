# Problem: Valid Parentheses (NeetCode 15) 
# Category: Stack 
# Time Complexity: O(N) - Single linear pass through the string of length N 
# Space Complexity: O(N) - Worst-case stack allocation when storing unmatched opening brackets

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in pairs:
                if stack and stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0
