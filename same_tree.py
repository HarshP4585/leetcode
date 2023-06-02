# Problem: https://leetcode.com/problems/same-tree/

# Solution 1:
# Recusion: use recursion and check root node, except Attribute error for node sub-trees
# Time: O(n), Space: O(1)

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, p: TreeNode, q: TreeNode):
        # base case
        if not p and not q:
            return
        if p.val == q.val:
            self.dfs(p.left, q.left)
            self.dfs(p.right, q.right)
        else:
            raise AttributeError
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        try:
            self.dfs(p, q)
        except AttributeError:
            return False
        return True

print(Solution().isSameTree(
    TreeNode(1,
        TreeNode(2),
        TreeNode(3)
    ),
    TreeNode(1,
        TreeNode(2),
        TreeNode(3)
    )
))
