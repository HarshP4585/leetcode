# Problem: https://leetcode.com/problems/subtree-of-another-tree/

# Solution 1:
# 

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def equality(self, root: TreeNode, subRoot: TreeNode):
        if not root and not subRoot:
            return True
        
        if root.val != subRoot.val:
            raise AttributeError
        
        self.equality(root.left, subRoot.left)
        self.equality(root.right, subRoot.right)
        
        return True
    
    def bfs(self, root: TreeNode, subRoot: TreeNode):
        queue = [root]
        
        for node in queue:
            if node.val == subRoot.val:
                try:
                    return self.equality(node, subRoot)
                except AttributeError:
                    pass
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.bfs(root, subRoot)

print(Solution().isSubtree(
    TreeNode(-1,
        TreeNode(-4,
            TreeNode(-6,
                right=TreeNode(-5)
            ),
            TreeNode(-2)
        ),
        TreeNode(8,
            TreeNode(3,
                TreeNode(0),
                TreeNode(7)
            ),
            TreeNode(9)
        )
    ),
    TreeNode(3,
        TreeNode(0),
        TreeNode(2)
    )
))
