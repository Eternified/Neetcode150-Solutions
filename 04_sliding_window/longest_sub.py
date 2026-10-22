# Problem: Longest Substring Without Repeating Characters (NeetCode 23) 
# Category: Sliding Window 
# Time Complexity: O(N) - Linear time; each character is processed at most twice by the pointers 
# Space Complexity: O(N) - Linear space required for the set tracking unique characters in the window

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_concurrent = 0 
        seen = set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.discard(s[l])
                l += 1

            seen.add(s[r])
            if max_concurrent < r - l + 1:
                max_concurrent = r - l + 1
        return max_concurrent
