# Problem: https://leetcode.com/problems/two-sum/

# Solution 1:
# Brute Force: Check every combination in the list make up the target
# Time: O(n^2), Space: O(1)

# Solution 2:
# Use hashmap to store the visited number and index, check if the (target - current) exists in the map
# Time: O(n), Space: O(n)

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = dict()
        
        for i, num in enumerate(nums):
            if visited.__contains__(target - num):
                return [i, visited[target - num]]
            visited[num] = i

print(Solution().twoSum([3, 2, 4], 6))
