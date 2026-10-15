# Problem: Contains Duplicate (NeetCode 1)
# Category: Arrays & Hashing
# Time Complexity: O(N) - Single pass traversal through the array
# Space Complexity: O(N) - Hash set memory scales linearly with unique elements
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False
