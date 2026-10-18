# Problem: Two Sum II - Input Array Is Sorted (NeetCode 11) 
# Category: Two Pointers 
# Time Complexity: O(N) - Linear pass scanning inward from both ends 
# Space Complexity: O(1) - Constant space using only two integer pointers

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            current_sum = numbers[left] + numbers[right]
            
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1 
            else:
                right -= 1
