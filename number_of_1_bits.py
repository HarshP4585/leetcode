# Problem: https://leetcode.com/problems/number-of-1-bits/

# Solution 1:
# Use %2 and shift the bits by 1
# Time: O(32) (32 bit input), Space: O(1)

# Solution 2:
# https://www.youtube.com/watch?v=5Km3utixwZs&t=340s

class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        
        while n != 0:
            counter += n % 2
            n = n > 1
        
        return counter

print(Solution().hammingWeight(00000000000000000000000000001011))
