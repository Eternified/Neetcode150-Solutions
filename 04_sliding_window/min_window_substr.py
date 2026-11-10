# Problem: Minimum Window Substring (NeetCode 26) 
# Category: Sliding Window 
# Time Complexity: O(N) - Linear time; where N is the length of s, as each character is processed at most twice by the two pointers 
# Space Complexity: O(M) - Space for frequency maps, where M is the number of unique characters in t (or O(1) bounded by fixed alphabet size)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return False

        t_count = {}

        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        window_count = {}
        have, need = 0, len(t_count)
        res, res_len = [-1, -1], float("inf")
        l = 0

        for r in range(len(s)):
            char = s[r]
            window_count[char] = window_count.get(char, 0) + 1

            if char in t_count and window_count[char] == t_count[char]:
                have += 1

            while have == need:
    
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                left_char = s[l]
                window_count[left_char] -= 1
                
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    have -= 1
                
                l += 1

        l, r = res

        return s[l : r + 1] if res_len != float("inf") else ""
