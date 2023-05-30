# Problem: https://leetcode.com/problems/merge-two-sorted-lists/

# Solution 1:
# Use dummy node and pointer for each lists to compare and insert correct ordered list in one list
# Time: O(n), Space: O(1)

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prev_list1 = head = ListNode(-1)
        prev_list1.next = list1
        
        while list1 and list2:
            if list1.val < list2.val:
                prev_list1 = list1
                list1 = list1.next
                continue
            prev_list1.next = list2
            list2 = list2.next
            prev_list1 = prev_list1.next
            prev_list1.next = list1
        
        if not list1:
            prev_list1.next = list2
        else:
            prev_list1.next = list1
        
        return head.next

print(Solution().mergeTwoLists(
    ListNode(1, ListNode(2, ListNode(4))),
    ListNode(1, ListNode(3, ListNode(5)))
))
