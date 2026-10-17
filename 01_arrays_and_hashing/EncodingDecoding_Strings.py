# Problem: Encode and Decode Strings (NeetCode 6) 
# Category: Arrays & Hashing 
# Time Complexity: O(N) - Single pass traversal over all characters
# Space Complexity: O(N) - Memory scales linearly with total characters

class Solution:
    def encode(self, strs: List[str]) -> str:
        # Turning a list of strings into a string

        encoded = []
        for str in strs:
            encoded.append(f"{len(str)}#{str}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        # Turning a string into a list of strings
        
        decoded = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length

            decoded.append(s[start:end])

            i = end
        return decoded
