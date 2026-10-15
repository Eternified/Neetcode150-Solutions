# Problem: Top K Frequent Elements (LeetCode 347 / NeetCode 5)
# Category: Arrays & Hashing
# Time Complexity: O(N) — Linear time to count, bucket, and collect elements
# Space Complexity: O(N) — Memory slots allocated for the count map and bucket lists

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequencies = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        answer = []
        
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
            
        for num, count in frequencies.items():
            buckets[count].append(num)
            
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                answer.append(num)
                if len(answer) == k:
                    return answer
