# Problem: https://leetcode.com/problems/balanced-binary-tree/

# Solution 1:
# Brute force: do a recursive dfs to determine height of left and right sub-tree for every node from root and compare heights
# Time: O(n^2), Space: O(1)

# Solution 2:
# Recursion: go bottom-up and compare heights for balance of left and right sub-tree
# Time: O(n), Space: O(1)

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    valid = {1, 0, -1}
    def dfs(self, node: TreeNode):
        
        left = 0
        if node.left:
            left = 1 + self.dfs(node.left)
        
        right = 0
        if node.right:
            right = 1 + self.dfs(node.right)
        
        if self.valid.__contains__(left - right):
            # max height of the sub-tree
            return max(left, right)
        raise ValueError
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        try:
            self.dfs(root)
        except ValueError:
            return False
        return True

print(Solution().isBalanced(
    TreeNode(3,
        TreeNode(9),
        TreeNode(20,
            TreeNode(15),
            TreeNode(7)
        )
    )
))
