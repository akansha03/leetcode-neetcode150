"""
Problem: [Valid Anagram]
Link: https://leetcode.com/problems/valid-anagram/
Difficulty: [Easy]
Topics: [Array, Hash Table]

Pattern: [Count the frequency of the characters of first string using hash table and reduce the count while iterating the second]
Key Insight: [If at last the count is 0 then both strings are anagram otherwise they are not]

Time Complexity: O(n)
Space Complexity: O(n)

Solved: [28/10/2025]
Revised: [19/11/2025], [], []
Confidence: ⭐⭐⭐⭐⭐
"""

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if not s and not t:
            return True

        if not s or not t:
            return False

        count = defaultdict(int)
        for c in s:
            count[c] += 1
        for d in t:
            count[d] -= 1
        for k in count.values():
            if k!=0:
                return False
        return True

if __name__ == "__main__":
    sol = Solution()
    assert sol.isAnagram('rat', 'car') == False
    assert sol.isAnagram('hello', 'elloh') == True
    assert sol.isAnagram('anagram', 'nagrama') == True
    assert sol.isAnagram('anagram', '') == False
    assert sol.isAnagram('', 'nagrama') == False
    assert sol.isAnagram('','' ) == True
    print("✅ All tests passed!")