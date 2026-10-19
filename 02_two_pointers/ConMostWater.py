# Problem: Container With Most Water (NeetCode 13) 
# Category: Two Pointers 
# Time Complexity: O(N) - Single linear pass scanning inward from both ends 
# Space Complexity: O(1) - Constant space using integer pointers and scalar variables

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l, r = 0, len(heights) - 1

        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            max_area = max(max_area, (width * height))
        
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area
