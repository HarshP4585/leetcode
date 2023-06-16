# Problem: https://leetcode.com/problems/min-cost-climbing-stairs/

# Solution 1:
# Using DP and recursion: Use DFS and bottom-up approach to find the minimum cost with caching
# Time: O(n), Space: O(n)

# Solution 2:
# Using DP and iteration
# Time: O(n), Space: O(1)

from typing import List

class Solution:
    cache = {}
    def dfs(self, step):
        if step == self.top:
            return self.cost[step]
        if step > self.top:
            return 0
        step_1 = self.dfs(step + 1)
        self.cache[step + 1] = step_1
        step_1 += self.cost[step]
        if step + 2 in self.cache:
            step_2 = self.cache[step + 2] + self.cost[step]
        else:
            step_2 = self.dfs(step + 2)
            self.cache[step + 2] = step_2
            step_2 += self.cost[step]
        return min(step_1, step_2)
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.top = len(cost) - 1
        self.cost = cost
        self.cache.clear()
        print(self.cache)
        return min(self.dfs(0), self.cache.get(1, float("inf")))

# print(Solution().minCostClimbingStairs([10,15,20]))
print(Solution().minCostClimbingStairs([1,100,1,1,1,100]))
