# Problem: https://leetcode.com/problems/3sum/

# Solution 1:
# Use two pointers and loop over every number and use twoSum for rest of the numbers to check the summation
# Time: O(n^2), Space: O(n)

from typing import List

class Solution:
    
    # very bad code, need more optimisation
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        visited = set()
        to_return = set()
        
        for i, num in enumerate(nums):
            if visited.__contains__(num):
                continue
            
            start = 0
            end = len(nums) - 1
            
            while (start < end):
                if start == i:
                    start += 1
                    continue
                if end == i:
                    end -= i
                    continue
                
                if (nums[start] + nums[end] > -num):
                    end -= 1
                elif (nums[start] + nums[end] < -num):
                    start += 1
                else:
                    triplet = tuple(sorted([nums[start], nums[end], num]))
                    if not to_return.__contains__(triplet):
                        to_return.add(triplet)
                    start += 1
        
        return to_return

print(Solution().threeSum([-1,0,1,2,-1,-4]))