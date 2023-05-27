# Problem: https://leetcode.com/problems/valid-palindrome/

# Solution 1:
# Loop over the string store the to_check string by removing the special characters and converting into lower case
# Check the string by reversing
# Time: O(n), Space: O(n)

# Solution 2:
# Use two-pointers
# Time: O(n/2), Space: O(n)

class Solution:
    alpha = {
        "A": "a",
        "B": "b",
        "C": "c",
        "D": "d",
        "E": "e",
        "F": "f",
        "G": "g",
        "H": "h",
        "I": "i",
        "J": "j",
        "K": "k",
        "L": "l",
        "M": "m",
        "N": "n",
        "O": "o",
        "P": "p",
        "Q": "q",
        "R": "r",
        "S": "s",
        "T": "t",
        "U": "u",
        "V": "v",
        "W": "w",
        "X": "x",
        "Y": "y",
        "Z": "z",
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9"
    }
    def isPalindrome(self, s: str) -> bool:
        start = 0
        last = len(s) - 1
        _all = self.alpha.keys() | self.alpha.values()
        while start < last:
            c1 = s[start]
            c2 = s[last]
            if c1 in _all and c2 in _all:
                c1 = self.alpha.get(c1, c1)
                c2 = self.alpha.get(c2, c2)
                if c1 == c2:
                    start += 1
                    last -= 1
                    continue
                else:
                    return False
            if c1 not in _all:
                start += 1
            if c2 not in _all:
                last -= 1
        return True

print(Solution().isPalindrome("0P"))
