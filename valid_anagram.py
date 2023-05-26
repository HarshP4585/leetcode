# Problem: https://leetcode.com/problems/valid-anagram/

# Solution 1:
# Count the occurrences of each character in each string, loop over the keys of one and compare with other
# Time: O(s + t), Space: O(s)

# Solution 2:
# Order both the strings and compare
# Time: O(nlogn), Space: O(1)

# Solutuon 3: https://leetcode.com/problems/valid-anagram/submissions/957503312/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = dict()
        
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        
        for char in t:
            if counter.get(char, 0) > 0:
                counter[char] = counter.get(char) - 1
                if counter[char] == 0:
                    counter.pop(char)
                continue
            return False

        return counter == {}

print(Solution().isAnagram("anagram", "nagaram"))
