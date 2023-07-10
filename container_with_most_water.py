# Problem: https://leetcode.com/problems/container-with-most-water/

# Solution 1:
# Use two-pointers and find the max-area between the pointers
# Time: O(n), Space: O(1)

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        max_area = 0
        
        while (start < end):
            max_area = max(
                max_area,
                min(height[start], height[end]) * (end - start)
            )
            
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        
        return max_area

print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))
