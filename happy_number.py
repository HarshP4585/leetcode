# Problem: https://leetcode.com/problems/happy-number/

# Solution 1:
# Use cache to store previous numbers and generate sum of squares until the number is found in the cache or number is 1

# Solution 2:
# Linked List Cycle

class Solution:
    def isHappy(self, n: int) -> bool:
        sum = 0
        cache = set()
        while n not in cache and n != 1:
            cache.add(n)
            while n != (n % 10):
                sum += ((n % 10) ** 2)
                n //= 10
            n = sum + (n ** 2)
            sum = 0
        return n == 1

print(Solution().isHappy(2))
