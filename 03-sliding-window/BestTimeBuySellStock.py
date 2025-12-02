"""
Problem: Best Time to Buy and Sell Stock
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Difficulty: [Easy]
Topics: [Array]

Pattern: [Sliding Window]

Key Insight:

* Take 0th element as the min_price and update it once u find the next minimum price.
* For the maximum profit, subtract the prices with all the min_price to capture the maximum profit

Time Complexity: O(n)
Space Complexity: O(1)

Solved: [22/11/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐⭐⭐
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        min_price, max_profit = prices[0], 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price-min_price)
        return max_profit

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxProfit([10,1,5,6,7,1]) == 6
    assert sol.maxProfit([10,8,7,5,2]) == 0
    print("✅ All tests passed!")