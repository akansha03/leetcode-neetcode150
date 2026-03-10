"""
Problem: [Longest Palindromic Substring]
Link: https://leetcode.com/problems/longest-palindromic-substring/description/
Difficulty: [Medium]
Topics: [String, DP, Recursion, Backtracking]

Pattern: [Expand Around the corner]
Key Insight: [This problem could be solved with dp as well but expand around the corner is easier once understanding is
clear. Create a function expand with two parameters - left and right, check if s[left] and s[right] are equal or not, if
yes, decrease left by 1 and increase right by 1 so that it could be checked whether those string indices are same or
not - return the substring from left to right.]

In the main loop, run expand from (i, i) and (i, i+1), check the returned string - longer one should be stored as result.]

Time Complexity: O(n^2)
Space Complexity: O(1)

Solved: [10/03/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def expand(left, right):
            while left>=0 and right<n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        longest = ''
        for i in range(n):

            # For odd there will be a middle element so same index will work
            p1 = expand(i, i)

            # For even length there will be two numbers in the middle
            p2 = expand(i, i+1)
            longer = p1 if len(p1)>len(p2) else p2
            longest = longer if len(longer) > len(longest) else longest
        return longest

if __name__ == "__main__":
    sol = Solution()
    assert sol.longestPalindrome("babad") == "bab"
    assert sol.longestPalindrome("cbbd") == "bb"
    print("✅ All tests passed!")