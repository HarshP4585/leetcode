# Problem: https://leetcode.com/problems/evaluate-reverse-polish-notation/

# Solution 1:
# Use stack and round the operation evaluation to zero (especially /)
# Time: O(n), Space: O(n)

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        counter = 0
        
        while counter < len(tokens):
            to_append = tokens[counter]
            if tokens[counter] in {"+", "-", "*", "/"}:
                n1 = stack.pop()
                n2 = stack.pop()
                to_append = int(eval("{} {} {}".format(n2, tokens[counter], n1)))
            stack.append(to_append)
            counter += 1
        
        return int(stack[0])

print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
