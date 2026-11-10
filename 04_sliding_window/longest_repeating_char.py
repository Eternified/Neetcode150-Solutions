# Problem: Longest Repeating Character Replacement (NeetCode 24) 
# Category: Sliding Window 
# Time Complexity: O(N) - Linear time; each character is processed at most twice by the pointers 
# Space Complexity: O(1) - Constant space; hash map holds at most 26 uppercase English letters

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        max_freq = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(max_freq, count[s[r]])

            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, (r - l + 1))
        return res
