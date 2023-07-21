# Problem: https://leetcode.com/problems/search-a-2d-matrix/

# Solution 1:
# Use 2 pointers (start and end) and binary search, populate the [row][col] based on the index and check the value of the mid pointer
# Time: O(log(m * n)), Space: O(1)

# Solution 2:
# Find the row to look for the target by comparing the last value of each row and run the binary search in that row

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        
        start = 0
        end = row * col - 1
        
        while start <= end:
            mid = (start + end) // 2
            mid_value = matrix[mid // col][mid % col]
            start_value = matrix[start // col][start % col]
            end_value = matrix[end // col][end % col]
            
            if start_value > target or end_value < target:
                break

            if mid_value == target:
                return True
            elif mid_value > target:
                end = mid - 1
            else:
                start = mid + 1
        
        return False

# print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
# print(Solution().searchMatrix([[1]], 2))
print(Solution().searchMatrix([[1,3,5]], 4))
