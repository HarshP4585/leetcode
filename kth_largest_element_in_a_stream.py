# Problem: https://leetcode.com/problems/kth-largest-element-in-a-stream/

# Solution 1:
# Use min-heap to store the k elements, when add function will be called, push-pop operation will be performed followed by lookup at [0] which will be kth largest element
# Time: O(logn) (init) O(mlogn) (add), Space: O(n)

# Solution 2:
# Use max-heap (-ve) and store k elements in min-heap, when add function will be called, if the [0] element is greater than the val, the [0] is kth largest element, else, push-pop operation followed by [0] lookup is kth largest element
# Time: O(logn + logk) (init) O(mlogn) (add), Space: O(n)

from typing import List
import heapq

class KthLargest:
    
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = [-i for i in nums] # max-heap
        heapq.heapify(self.nums)
        self.k_nums = [] # min-heap
        for i in range(k):
            if self.nums:
                self.k_nums.append(-heapq.heappop(self.nums))
        heapq.heapify(self.k_nums)
    
    def add(self, val: int) -> int:
        if len(self.k_nums) < self.k:
            # will be heapified automatically
            heapq.heappush(self.k_nums, val)
        elif val > self.k_nums[0]:
            # will be heapified automatically
            heapq.heappop(self.k_nums)
            heapq.heappush(self.k_nums, val)
        return self.k_nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(3, [4,5,8,2])
# print(obj.add(3))
# print(obj.add(5))
# print(obj.add(10))
# print(obj.add(9))
# print(obj.add(4))

# obj = KthLargest(1, [])
# print(obj.add(-3))
# print(obj.add(-2))
# print(obj.add(-4))
# print(obj.add(0))
# print(obj.add(4))

obj = KthLargest(2, [0])
print(obj.add(-1))
print(obj.add(1))
print(obj.add(-2))
print(obj.add(-4))
print(obj.add(3))
