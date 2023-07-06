# Problem: https://leetcode.com/problems/longest-consecutive-sequence/

# Solution 1:
# Sort and check for sequence
# Time: O(nlogn), Space: O(1)

# Solution 2:
# Create set of nums and look for start of element of a sequence by looking for (num - 1) in the set and create the longest sequence possible
# Time: O(n), Space: O(n)

from typing import List
import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        longest = 0
        prev = float("-inf")
        to_return = longest
        
        for i in range(len(nums)):
            this = heapq.heappop(nums)
            if this == prev:
                continue
            elif this == prev + 1:
                longest += 1
            else:
                to_return = max(to_return, longest)
                longest = 1
            prev = this
        to_return = max(to_return, longest)
        
        return to_return

print(Solution().longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))