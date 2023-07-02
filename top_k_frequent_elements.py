# Problem: https://leetcode.com/problems/top-k-frequent-elements/

# Solution 1:
# Use hash map to count the frequency, followed by heap to get top k elements as per their frequency
# Time: O(n + m*logm + k), Space: O(2m + k)

# Solution 2:
# Using bucket sort: Use hash map to count the frequency and add the frequency of values in the list
# Time: O(2n), Space: O(m + n)

from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = dict()
        heap = []
        heapq.heapify(heap)
        
        for num in nums:
            map[num] = map.get(num, 0) + 1
        
        for key, value in map.items():
            heapq.heappush(heap, [-value, key])
        
        to_return = []
        
        for _ in range(k):
            frequency, value = heapq.heappop(heap)
            to_return.append(value)
        
        return to_return

print(Solution().topKFrequent([1,1,1,2,2,3], 2))
