# Problem: https://leetcode.com/problems/plus-one/

# Solution 1:
# Reverse the array and maintain a carry starting from 1, finally reverse the array
# Time: O(2n), Space: O(1)

# Solution 2:
# Find the first of consecutive 9s, add 1 to the previous element and change all 9s to 0
# Time: O(n), Space: O(1)

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        nine = length
        for i in range(length):
            if digits[length - 1 - i] == 9:
                nine = length - 1 - i
            else:
                break
        
        if nine == 0:
            digits[0] = 1
            for i in range(1, length):
                digits[i] = 0
            digits.append(0)
            return digits
        
        for i in range(nine, length):
            digits[i] = 0
        digits[nine - 1] += 1
        return digits

print(Solution().plusOne([9,9,9,9]))
