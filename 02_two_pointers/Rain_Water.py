# Problem: Trapping Rain Water (NeetCode 14) 
# Category: Two Pointers 
# Time Complexity: O(N) - Single linear pass inward from both ends 
# Space Complexity: O(1) - Constant auxiliary space using two pointers and scalar max tracking variables

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        t_area = 0
        l_wall_max = 0
        r_wall_max = 0

        while l < r:
            l_wall_max = max(l_wall_max, height[l])
            r_wall_max = max(r_wall_max, height[r])

            if l_wall_max < r_wall_max:
                if l_wall_max > height[l]:
                    t_area += l_wall_max - height[l]
                l += 1
            else:
                if r_wall_max > height[r]:
                    t_area += r_wall_max - height[r]
                r -= 1
        return t_area
