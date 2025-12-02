"""
Problem: [Longest Repeating Character Replacement]
Link: https://leetcode.com/problems/longest-repeating-character-replacement/

Difficulty: [Medium]
Topics: [Array, Hash Table]
Pattern: [Sliding Window]

Key Insight:

# Sliding window: expand right, count frequencies, track max_count.
# Window is valid if (window_size - max_count) <= k.
# If invalid, move left pointer and shrink window.
# Update max length for every valid window.
# Classic pattern: grow window → check validity → shrink if needed.

Time Complexity: O(n)
Space Complexity: O(n)

Solved: [23/11/2025]
Revised: [01/12/2025], [], []
Confidence: ⭐⭐
"""

from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count, max_count = defaultdict(int), 0
        left, length = 0, 0
        for right in range(len(s)):
            count[s[right]] += 1
            max_count = max(max_count, count[s[right]])

            # valid window is : right-left+1-max_count-k
            while right-left+1-max_count-k > 0:
                count[s[left]] -= 1
                left += 1
            length = max(length, right-left+1)
        return length

if __name__ == "__main__":
    sol = Solution()
    assert sol.characterReplacement("ABAB", 2) == 4
    assert sol.characterReplacement("AABABBA", 1) == 4
    print("✅ All tests passed!")