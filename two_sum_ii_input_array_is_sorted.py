# Problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# Solution 1:
# For every number loop over every number and check the target
# Time: O(n^2), Space: O(1)

# Solution 2:
# Use two pointers and change the start or end pointer based on certain condition
# Time: O(n), Space: O(1)

from typing import List

class Solution:    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        
        while (numbers[start] + numbers[end]) != target:
            if numbers[start] > (target - numbers[end]):
                end -= 1
            else:
                start += 1
        
        return [start + 1, end + 1]

print(Solution().twoSum([-1,-1,-1,-1,-1,1,1], 2))
