"""
Problem: [Valid Palindrome]
Link: https://leetcode.com/problems/valid-palindrome/description/
Difficulty: [Easy]
Topics: [Two Pointer Array]

Pattern: [Two pointer]
Key Insight: [This is a pattern where left pointer will start from 0th index and right from the
last index and will check if alphanumeric values at those indices are equal or not, if not return False
Apply lower() to check for the accurate character
]

Time Complexity: O(n)
Space Complexity: O(1)

Solved: [19/11/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐⭐⭐
"""

from typing import List

class Solution:
    def valid_palindrome(self, s: str) -> bool:
        if not s:
            return True

        left, right = 0, len(s)-1
        while left<right:
            while left<right and not s[left].isalnum():
                left += 1
            while left<right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

if __name__ == "__main__":
    sol = Solution()
    assert sol.valid_palindrome('A man, a plan, a canal: Panama') == True
    assert sol.valid_palindrome('race a car') == False
    assert sol.valid_palindrome(" ") == True
    print("✅ All tests passed!")