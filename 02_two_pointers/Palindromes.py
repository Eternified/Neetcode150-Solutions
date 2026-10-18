# Problem: Valid Palindrome (NeetCode 10) 
# Category: Two Pointers 
# Time Complexity: O(N) - Linear pass regex filtration and string reversal 
# Space Complexity: O(N) - Allocates memory for filtered and reversed string copies

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        return newstr == newstr[::-1]
