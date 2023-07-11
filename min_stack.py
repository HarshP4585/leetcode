# Problem: https://leetcode.com/problems/min-stack/

# Solution 1:
# Use linked-list

# Solution 2:
# Use list

# Using Linked-List
# class ListNode:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next

# class MinStack:

#     def __init__(self):
#         self.stack = None
#         self.min = None

#     def push(self, val: int) -> None:
#         if not self.stack:
#             self.stack = ListNode(val)
#         else:
#             self.stack = ListNode(val, self.stack)
        
#         if not self.min:
#             self.min = ListNode(val)
#         else:
#             self.min = ListNode(min(val, self.min.value), self.min)

#     def pop(self) -> None:
#         self.stack = self.stack.next
#         self.min = self.min.next

#     def top(self) -> int:
#         return self.stack.value

#     def getMin(self) -> int:
#         return self.min.value

# Using List
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min:
            self.min.append(val)
        else:
            self.min.append(min(val, self.min[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(-2)
# obj.push(0)
# obj.push(-3)
# print(obj.getMin())
# obj.pop()
# print(obj.top())
# print(obj.getMin())
