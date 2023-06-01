# Problem: https://leetcode.com/problems/diameter-of-binary-tree/

# Solution 1:
# Brute force: find the lowest node from every node (starting from the root) as the root node and return the max diameter by summing left and right depth
# Time: O(n^2), Space: O(1)

# Solution 2:
# Recursion: solve the sub-problem and go bottom-up
# Time: O(n), Space: O(1)

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    dia = 0
    def dfs(self, node: TreeNode):
        left = 0
        if node.left:
            left = 1 + self.dfs(node.left)
        
        right = 0
        if node.right:
            right = 1 + self.dfs(node.right)
        
        self.dia = max(self.dia, left + right)
        
        return max(left, right)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.dia

print(Solution().diameterOfBinaryTree(
    TreeNode(1,
        TreeNode(2,
            TreeNode(3,
                TreeNode(5,
                    TreeNode(7),
                    TreeNode(8)
                ),
                TreeNode(6,
                    TreeNode(9),
                    TreeNode(10,
                        TreeNode(11),
                        TreeNode(12)
                    )
                )
            ),
            TreeNode(4)
        )
    )
))
