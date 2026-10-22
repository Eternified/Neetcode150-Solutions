# Problem: Largest Rectangle in Histogram (NeetCode 20) 
# Category: Stack 
# Time Complexity: O(N) - Linear time; each element is pushed and popped at most once 
# Space Complexity: O(N) - Linear space for the monotonic stack

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i

            while stack and stack[-1][-1] > h:
                idx, height = stack.pop()

                max_area = max(max_area, ((i - idx) * height))
                start = idx

            stack.append((start, h))
        
        for idx, height in stack:
            max_area = max(max_area, (height * (len(heights) - idx)))

        return max_area
