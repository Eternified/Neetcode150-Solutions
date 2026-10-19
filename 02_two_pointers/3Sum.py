# Problem: 3Sum (NeetCode 12) 
# Category: Two Pointers 
# Time Complexity: O(N^2) - Sorting takes O(N log N) and outer loop with inner two pointers scan takes O(N^2) 
# Space Complexity: O(1) or O(N) - O(1) extra auxiliary space, or O(N) depending on Python's Timsort implementation

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] > 0:
                break

            l, r = i + 1, n - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total == 0:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return output
