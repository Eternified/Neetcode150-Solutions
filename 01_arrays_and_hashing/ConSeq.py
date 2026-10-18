# Problem: Longest Consecutive Sequence (NeetCode 9) 
# Category: Arrays & Hashing 
# Time Complexity: O(N) - Linear scan where each element is visited at most twice 
# Space Complexity: O(N) - Hash set stores up to N elements for O(1) lookups

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
