# Problem: https://leetcode.com/problems/reverse-linked-list/

# Solution 1:
# Iteratively using two-pointers
# Time: O(n), Space: O(1)

# Soultion 2:
# Recursively

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # using iteration
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        next = head.next
        head.next = None
        while next:
            temp = next.next
            next.next = head
            head = next
            next = temp
        return head

print(Solution().reverseList(
    ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
))
