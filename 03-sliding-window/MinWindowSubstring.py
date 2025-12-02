"""
Problem: [Minimum Window Substring]
Link: https://leetcode.com/problems/minimum-window-substring/description/
Difficulty: [Hard]
Topics: [Array, Hash Table]

Pattern: [Frequency-based sliding window pattern]

Key Insight:
- need map (constant)
- window map (dynamic)
- have counter (tracks satisfied unique chars)
- Expand: add to window, check if threshold crossed
- Shrink: check if threshold will break, remove from window
- Philosophy is consume + check+ release

Time Complexity: O(len(t) * len(s))
Space Complexity: O(n)

Solved: [23/11/2025]
Revised: [], [], []
Confidence: ⭐⭐
"""

from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m,n = len(s), len(t)
        if m<n:
            return ""
        freq = defaultdict(int)
        for c in t:
            freq[c] += 1
        left, min_len, sIndex, count = 0, float('inf'), -1, 0
        for right in range(m):
            if freq[s[right]] > 0:
                count += 1
            freq[s[right]] -= 1
            while count == n:
                if right-left+1 < min_len:
                    min_len = min(min_len, right-left+1)
                    sIndex = left
                freq[s[left]] +=1
                if freq[s[left]] > 0:
                    count -= 1
                left += 1
        return s[sIndex: sIndex+min_len] if sIndex != -1 else ""

if __name__ == "__main__":
    sol = Solution()
    assert sol.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert sol.minWindow("a", "a") == "a"
    assert sol.minWindow("a", "aa") == ""
    print("✅ All tests passed!")