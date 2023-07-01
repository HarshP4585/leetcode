# Problem: https://leetcode.com/problems/group-anagrams/

# Solution 1:
# Sort the string and compare
# Time: O(m*nlong), Space: O(m)

# Solution 2:
# Use list of count of chars for every word and store as a key in a hash-map
# Time: O(m*n), Space: O(m)

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = dict()
        to_return = []
        position_counter = 0
        
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in map:
                map[sorted_word] = position_counter
                position_counter += 1
                to_return.append([])
            
            to_return[map.get(sorted_word)].append(word)
        
        return to_return

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))