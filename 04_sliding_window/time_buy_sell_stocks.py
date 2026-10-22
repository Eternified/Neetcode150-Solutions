# Problem: Best Time to Buy and Sell Stock (NeetCode 22) 
# Category: Sliding Window 
# Time Complexity: O(N) - Single pass through the prices array 
# Space Complexity: O(1) - Constant space used for pointers and tracking max profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        max_profit = 0 

        for r in range(1, len(prices)):
            if prices[l] < prices[r]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r

        return max_profit
