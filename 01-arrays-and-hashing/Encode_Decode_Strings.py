"""
Problem: [Encode and Decode Strings]
Link: https://neetcode.io/problems/string-encode-and-decode?list=neetcode150
Difficulty: [Medium]
Topics: [Array, String]

Pattern: [For encoding use a character not UTF-8 to concatenate it and split the string - adding the same character regex]
Key Insight: [While encoding the character will be appended at the end so post splitting return the slice [:-1]

Time Complexity: O(n)
Space Complexity: O(n)

Solved: [29/10/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐⭐⭐
"""

from typing import List
class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ''
        temp = []
        for s1 in strs:
            temp.append(s1+ '+')
        return ''.join(temp)

    def decode(self, s: str) -> List[str]:
        s_temp = s.split('+')
        return s_temp[:-1]

if __name__ == "__main__":
    sol = Solution()
    so = sol.encode(["neet","code","love","you"])
    assert sol.decode(so) == ["neet","code","love","you"]
    print("✅ All tests passed!")