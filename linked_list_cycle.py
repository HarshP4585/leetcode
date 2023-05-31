# Problem: https://leetcode.com/problems/linked-list-cycle/

# Solution 1:
# Maintain a hashset of visited nodes and check if the current is in the set
# Time: O(n), Space: O(n)

# Solution 2:
# Use two-pointers, increment first pointer by 1 and other by 2. If they meet at a location then there is loop
# Time: O(n), Space: O(1)

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p = head
        q = head
        
        while p and q:
            p = p.next
            q = q.next
            if not q:
                continue
            q = q.next
            
            if p is q:
                return True
        
        return False

n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(0)
n4 = ListNode(4)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n2

print(Solution().hasCycle(None))
