# Problem: https://leetcode.com/problems/climbing-stairs/

# Solution 1:
# Iteration:

# Solution 2:
# Recursion:

# Solution 3:
# 

class Solution:
    # cache = {0: 0}
    
    # iteration
    # def climbStairs(self, n: int) -> int:
    #     prev_1 = 0
    #     prev_2 = 1
    #     to_return = 0
    #     for i in range(1, n + 1):
    #         to_return = prev_1 + prev_2
    #         prev_1 = prev_2
    #         prev_2 = to_return
    #     return to_return
    
    # def fib(self, n: int):
    #     if n <= 1:
    #         return n
    #     f1 = self.fib(n - 1)
    #     self.cache[n - 1] = f1
    #     f2 = self.cache.get(n - 2)
    #     return f1 + f2
    
    # fibonacci and caching: DP
    # def climbStairs(self, n: int) -> int:
    #     return self.fib(n + 1)
    
    def subSteps(self, n: int, cache: dict):
        if self.n == n:
            return 1
        if n > self.n:
            return 0
        step_1 = self.subSteps(n + 1, cache)
        cache[n + 1] = step_1
        if n + 2 in cache:
            step_2 = cache[n + 2]
        else:
            step_2 = self.subSteps(n + 2, cache)
            cache[n + 2] = step_2
        return step_1 + step_2
    
    # decision tree using DFS and caching: DP
    def climbStairs(self, n: int) -> int:
        if n in {1, 2}:
            return n
        self.n = n
        return self.subSteps(0, dict())

s = Solution()
print(s.climbStairs(38))
print(s.climbStairs(4))
