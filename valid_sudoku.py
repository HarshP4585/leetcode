# Problem: https://leetcode.com/problems/valid-sudoku/

# Solution 1:
# Create a function for determining the duplicate number using hash-set, loop over the rows and check for duplicates and create a (3 * 3) block rows and call the duplicate on the (3 * 3) rows every 3rd iteration on rows. Loop on columns and look for duplicates
# Time: , Space: 

# Solution 2:
# Use different hash-map of hash-sets for rows, cols and (3 * 3) squares to determine the values present in the area
# Time: , Space:

from typing import List

class Solution:
    def contains_duplicate(self, nums):
        hash_set = set()
        
        for num in nums:
            if num == ".":
                continue
            
            if num in hash_set:
                return True
            hash_set.add(num)
        
        return False
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        inner_blocks = [[], [], []]
        for i, row in enumerate(board):
            if self.contains_duplicate(row):
                return False
            
            k = 0
            for j in range(3):
                inner_blocks[j].extend(board[i][k:k + 3])
                k += 3
            
            if (i + 1) % 3 == 0:
                try:
                    for block in inner_blocks:
                        if self.contains_duplicate(block):
                            return False
                finally:
                    inner_blocks = [[], [], []]
        
        for col in range(9):
            cols = []
            for collector in range(9):
                cols.append(board[collector][col])
            
            if self.contains_duplicate(cols):
                return False
        
        return True

print(Solution().isValidSudoku(
    [[".",".",".",".",".",".","5",".","."]
    ,[".",".",".",".",".",".",".",".","."]
    ,[".",".",".",".",".",".",".",".","."]
    ,["9","3",".",".","2",".","4",".","."]
    ,[".",".","7",".",".",".","3",".","."]
    ,[".",".",".",".",".",".",".",".","."]
    ,[".",".",".","3","4",".",".",".","."]
    ,[".",".",".",".",".","3",".",".","."]
    ,[".",".",".",".",".","5","2",".","."]]
))
