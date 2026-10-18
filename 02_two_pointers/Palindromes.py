# Problem: Valid Palindrome (NeetCode 10) 
# Category: Two Pointers 
# Time Complexity: O(N) - Single pass scanning inward from both ends 
# Space Complexity: O(1) - Constant space processing string in-place class Solution:

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1

        while L < R:
            while L < R and not s[L].isalnum(): 
                L += 1
            while L < R and not s[R].isalnum(): 
                R -= 1
            if s[L].lower() != s[R].lower(): 
                return False 
            L += 1 
            R -= 1 
            
        return True
