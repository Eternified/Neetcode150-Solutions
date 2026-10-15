# Problem: Group Anagrams (LeetCode 49 / NeetCode 4)
# Category: Arrays & Hashing
# Time Complexity: O(M * N log N) — Loops through M strings, sorting each of length N
# Space Complexity: O(M * N) — Dictionary stores all characters of the input strings

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word not in groups:
                groups[sorted_word] = [word]
            else:
                groups[sorted_word].append(word)

        return list(groups.values())
