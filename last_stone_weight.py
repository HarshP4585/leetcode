# Problem: https://leetcode.com/problems/last-stone-weight/

# Solution 1:
# Use max-heap to get top 2 stones for smashing
# Time: O(nlogn), Space: O(n)

from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # max_stones = []
        # for stone in stones:
        #     heapq.heappush(max_stones, -stone)
        max_stones = [-i for i in stones]
        heapq.heapify(max_stones)
        
        while len(max_stones) > 1:
            x = -heapq.heappop(max_stones)
            y = -heapq.heappop(max_stones)
            
            diff = x - y
            if diff:
                heapq.heappush(max_stones, -diff)
        
        return 0 if not max_stones else -max_stones[0]

print(Solution().lastStoneWeight([2,7,4,1,8]))
