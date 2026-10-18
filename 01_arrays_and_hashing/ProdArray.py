# Problem: Product of Array Except Self (NeetCode 7) 
# Category: Arrays & Hashing 
# Time Complexity: O(N) - Two linear passes over the array 
# Space Complexity: O(1) - Output array does not count as extra space

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output
