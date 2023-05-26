# Problem: https://leetcode.com/problems/contains-duplicate/

# Solution 1:
# Brute Force: Compare an element with every element in the list to find the duplicate
# Time: O(n^2), Space: O(1)

# Solution 2:
# Sort the list and compare adjacent elements
# Time: O(nlogn), Space: O(1)

# Solution 3:
# Loop over the numbers and store in the hashset for lookup (in O(1) times) of duplicate element
# Time: O(n), Space: O(n)

# https://leetcode.com/problems/contains-duplicate/submissions/957492141/

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_hash = set()
        for num in nums:
            if num in nums_hash:
                return True
            nums_hash.add(num)
        return False

print(Solution().containsDuplicate([1, 2, 3, 4]))
