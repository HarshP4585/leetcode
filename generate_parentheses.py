# Problem: https://leetcode.com/problems/generate-parentheses/

# Solution 1:
# Brute Force: Start from "(" and add "(" or ")" based on the conditions and generate parentheses combinations
# Time: , Space: 

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        initial = [["(", 1, 0]]
        
        for _ in range(2 * n - 1):
            new = []
            for i in initial:
                if i[0][-1] == "(":
                    if i[1] < n:
                        new.append([i[0] + "(", i[1] + 1, i[2]])
                    new.append([i[0] + ")", i[1], i[2] + 1])
                else:
                    if i[1] > i[2]:
                        if i[1] < n:
                            new.append([i[0] + "(", i[1] + 1, i[2]])
                        new.append([i[0] + ")", i[1], i[2] + 1])
                    elif i[1] < n:
                        new.append([i[0] + "(", i[1] + 1, i[2]])
            initial = new
        
        return [i[0] for i in initial]

print(Solution().generateParenthesis(3))
