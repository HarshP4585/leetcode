# Problem: https://leetcode.com/problems/valid-parentheses/

# Solution 1:
# Use stack
#   closing tag cannot be added in empty array
#   closing of other tag cannot come before other tags

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        _map = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        closing = _map.keys()
        
        for char in s:
            if stack and stack[-1] in closing:
                return False
            if stack and _map.get(char) == stack[-1]:
                stack.pop(-1)
                continue
            stack.append(char)
        
        return not stack

print(Solution().isValid("{]"))
