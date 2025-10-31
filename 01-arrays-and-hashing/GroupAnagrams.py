"""
Problem: [Given an array of strings strs, group the anagrams together. You can return the answer in any order]
Link: https://leetcode.com/problems/group-anagrams/description/
Difficulty: [Medium]
Topics: [Array, Hash Table, etc.]

Pattern: [Use hashtable to calculate the frequency of all the strings and convert it to the string and use it as a key in a hashmap]
Key Insight: [Strings which are anagrams will probably have the same key so append them as values in the list]

Time Complexity: O(m*n) - n being the number of string and m being the length an individual string
Space Complexity: m * O(26) + O(n)

Solved: [28/10/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐⭐⭐
"""

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            freq = [0]*26
            for c in s:
                freq[ord(c)- ord('a')] += 1
            key = str(freq)
            result[key].append(s)
        return list(result.values())

    def groupAnagramsTuple(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            result[key].append(s)
        return list(result.values())

if __name__ == "__main__":
    sol = Solution()
    assert sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
    assert sol.groupAnagramsTuple(["eat", "tea", "tan", "ate", "nat", "bat"]) == [['eat', 'tea', 'ate'], ['tan', 'nat'],['bat']]
    print("✅ All tests passed!")