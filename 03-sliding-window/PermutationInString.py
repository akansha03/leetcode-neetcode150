"""
Problem: [Permutation in String]
Link: https://leetcode.com/problems/permutation-in-string/description/
Difficulty: [Medium]
Topics: [Array]

Pattern: [Fixed Sliding Window - length of the string s1]
Key Insight:
 * Calculate the frequency of s1 and store it in an array of size 26
 * Now the standard sliding window algorithm
 * Take elements of s2, add them in the array and keep on moving to the right
 * Check for an invalid window, i.e., in this case it will be any time the length of the window is more than the
   length of s1 then it's an invalid window
 * Decrease the frequency of the left element and increase left pointer by 1
 * Check if both the arrays are equal or not, if yes return True
 * Else, return False at the end

 * This could be solved using dictionary too, check for an invalid window and see if frequency of the
 character at the left pointer is 0 or not, if yes the pop it out.

 * This will help checking for both frequency dictionary.

Time Complexity: O(n)
Space Complexity: O(n)

Solved: [23/11/2025]
Revised: [30/11/2025], [], []
Confidence: ⭐⭐
"""
from typing import List
from collections import defaultdict

class Solution:

    # User Array to solve this problem
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2:
            return False
        m, n = len(s1), len(s2)
        if n<m:
            return False
        freqA = [0]*26
        freqB = [0]*26
        for c in s1:
            freqA[ord(c) - ord('a')] += 1
        left = 0
        for right in range(n):
            freqB[ord(s2[right]) - ord('a')] += 1
            while right - left + 1 > m:
                freqB[ord(s2[left]) - ord('a')] -= 1
                left += 1
            if freqA == freqB:
                return True
        return False

    # Use Dictionary to solve this problem
    def permutationString(self, s1, s2) -> bool:
        m,n = len(s1), len(s2)
        if n<m:
            return False
        if not s1 or not s2:
            return False
        freqA = defaultdict(int)
        freqB = defaultdict(int)
        for c in s1:
            freqA[c] += 1
        left = 0
        for right in range(n):
            freqB[s2[right]] += 1
            while right-left+1>m:
                freqB[s2[left]] -= 1
                if freqB[s2[left]] == 0:
                    freqB.pop(s2[left])
                left += 1
            if freqA == freqB:
                return True
        return False

if __name__ == "__main__":
    sol = Solution()
    assert sol.checkInclusion("ab", "eidbaooo") == True
    assert sol.checkInclusion("ab", "eidboaoo") == False
    assert sol.permutationString("ab", "eidbaooo") == True
    assert sol.permutationString("ab", "eidboaoo") == False
    print("✅ All tests passed!")