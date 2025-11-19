"""
Problem: Contains Duplicate
Link: https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy
Topics: [Array, Hash Set]

Pattern: Hash Set for uniqueness check
Key Insight: Compare set length with array length

Time Complexity: O(n)
Space Complexity: O(n)

Solved: 2024-10-28
Revised: [19/11/2025], [], []
Confidence: ⭐⭐⭐⭐⭐
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """Return True if any value appears at least twice in the array."""
        return len(nums) != len(set(nums))


if __name__ == "__main__":
    sol = Solution()
    assert sol.containsDuplicate([1, 2, 3, 1]) == True
    assert sol.containsDuplicate([1, 2, 3, 4]) == False
    assert sol.containsDuplicate([]) == False
    print("✅ All tests passed!")