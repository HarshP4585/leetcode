# Problem: https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Solution 1:
# Recusive DFS: max of left and right sub-tree depth
# Time: O(n), Space: O(1)

# Solution 2:
# Iterativs DFS

# Solution 3:
# BFS: use list to store the nodes at a particular level and maintain list for next level
# Time: O(n), Space: O(N)

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, node: TreeNode):
        if not node:
            return 0
        
        return 1 + max(self.dfs(node.left), self.dfs(node.right))
    
    def bfs(self, queue: List[TreeNode]):
        # can use single queue for looping instead of recursion
        temp_queue = []
        for node in queue:
            if not node:
                continue
            if node.left:
                temp_queue.append(node.left)
            if node.right:
                temp_queue.append(node.right)
        
        if not temp_queue:
            return 1
        
        return 1 + self.bfs(temp_queue)
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        # # only allowing not null values in the queue
        # return self.bfs([root])
        
        return self.dfs(root)

print(Solution().maxDepth(
    TreeNode(3,
        TreeNode(9),
        TreeNode(20,
            TreeNode(15),
            TreeNode(7)
        )
    )
))
