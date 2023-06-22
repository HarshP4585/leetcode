# Problem: https://leetcode.com/problems/single-number/

# Solution 1:
# Use hash set to store the visited nums
# Time: O(n), Space: O(n)

# Solution 2:
# Use bitmaniputation and perform XOR
# Time: O(n), Space: O(1)

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        visited = set()
        
        for num in nums:
            if visited.__contains__(num):
                visited.remove(num)
                continue
            
            visited.add(num)
        
        for i in visited:
            return i

print(Solution().singleNumber([4,1,2,1,2]))
