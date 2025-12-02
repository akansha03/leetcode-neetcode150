"""
Problem: [Longest Substring Without Repeating Characters]
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
Difficulty: [Medium]
Topics: [Array, Hash Set]

Pattern: [Sliding Window]
Key Insight: [Use set here to keep track of unique elements - whenever the element is duplicated remove it
and increase the value of left]

Time Complexity: O(n)
Space Complexity: O(n)

Solved: [22/11/2025]
Revised: [], [], []
Confidence: ⭐⭐
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = set()
        left, right, length = 0,0,0
        for right in range(len(s)):
            while s[right] in temp:
                temp.remove(s[left])
                left += 1
            temp.add(s[right])
            length = max(length, right-left+1)
        return length

if __name__ == "__main__":
    sol = Solution()
    assert sol.lengthOfLongestSubstring("abcabcbb") == 3
    assert sol.lengthOfLongestSubstring("pwwkew") == 3
    assert sol.lengthOfLongestSubstring("bbbbb") == 1
    print("✅ All tests passed!")