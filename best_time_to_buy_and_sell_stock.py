# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Solution 1:
# Use sliding window, maintain a max value of the window and fix the min value at the start of the window
# Time: O(n), Space: O(1)

# Solution 2:
# Use two pointers

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = float("inf")
        maxx = -1
        max_profit = 0
        
        for price in prices:
            maxx = max(maxx, price)
            if price < minn:
                max_profit = max(max_profit, maxx - minn)
                maxx = price
                minn = price
        return max(max_profit, maxx - minn)

print(Solution().maxProfit([2,4,1]))
