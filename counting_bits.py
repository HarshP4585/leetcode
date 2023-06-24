# Problem: https://leetcode.com/problems/counting-bits/

# Solution 1:
# Use caching and start from 0 up towards n and append the results in an array

# Solution 2:
# Using DP

from typing import List

class Solution:
    def count(self, n: int):
        ones = 0
        num = n
        while n != 0:
            if n in self.cache:
                ones += self.cache.get(n)
                break
            ones += n % 2
            n = n >> 1
        
        self.cache[num] = ones

    def countBits(self, n: int) -> List[int]:
        self.cache = dict()
        to_return = []
        ctr = 0
        while ctr != n + 1:
            self.count(ctr)
            to_return.append(self.cache.get(ctr))
            ctr += 1
        
        return to_return

print(Solution().countBits(5))
