# Problem: Permutation in String (NeetCode 25) 
# Category: Sliding Window 
# Time Complexity: O(N) - Linear time; where N is the length of s2, sliding a fixed window of size len(s1) across s2 
# Space Complexity: O(1) - Constant space; frequency maps store at most 26 lowercase English letters

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        l = 0
        s1_count = {}
        s2_count = {}

        for i in range(len(s1)):
            s1_count[s1[i]] = s1_count.get(s1[i], 0) + 1
            s2_count[s2[i]] = s2_count.get(s2[i], 0) + 1

        if s1_count == s2_count:
            return True
        
        for r in range(len(s1), len(s2)):
            right_char = s2[r]
            s2_count[right_char] = s2_count.get(right_char, 0) + 1

            left_char = s2[l]
            s2_count[left_char] -= 1
            if s2_count[left_char] == 0:
                del s2_count[left_char]
            
            l += 1

            if s1_count == s2_count:
                return True
                
        return False
