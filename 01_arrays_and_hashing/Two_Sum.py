# Problem: Two Sum (NeetCode 3)
# Category: Arrays & Hashing
# Time Complexity: O(N) - Single pass traversal checking complements in O(1) time
# Space Complexity: O(N) - Dictionary scales linearly to store values and indices

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        tracker = {} 
        
        for i in range(len(nums)):
            current_num = nums[i]
            complement = target - current_num
            
            if complement in tracker:
                return [tracker[complement], i]
        
            tracker[current_num] = i
