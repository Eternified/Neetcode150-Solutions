# Problem: Car Fleet (NeetCode 19) 
# Category: Stack
# Time Complexity: O(N log N) - Dominated by sorting the position-speed pairs 
# Space Complexity: O(N) - Linear space for the position-speed pairs and fleet stack

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pair = [[p, s] for p, s in zip(position, speed)]

        for p, s in sorted(pair, reverse=True):
            time = (target - p) / s
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
