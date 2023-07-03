# Problem: https://leetcode.com/problems/product-of-array-except-self/

# Solution 1:
# Use prefix product, start with last element in nums and multiply (index - 1) in prefix and right multiplier
# Time: O(n), Space: O(n)

# Solution 2:
# Store prefix in the same array followed by postfix
# Time: O(n), Space: O(1)

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        prev = 1
        
        for num in nums:
            prefix.append(num * prev)
            prev *= num
        
        right = 1
        
        for i, num in enumerate(nums[::-1]):
            left = 1
            if (len(nums) - i - 2) >= 0:
                left = prefix[len(nums) - i - 2]
            nums[len(nums) - i - 1] = right * left
            right *= num
        
        return nums

print(Solution().productExceptSelf([1,-1,0,9,-9]))
