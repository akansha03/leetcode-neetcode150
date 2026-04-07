"""
Problem: [Letter Combinations of a Phone Number]
Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Difficulty: [Combination + Recursion + Backtracking]
Topics: [Backtracking + Recursion]

Pattern: [Combination Problem]
Key Insight: [Form a HashMap for all the digits, and then iterate the characters corresponding the
digits and form a pair. Length of a single pair will be equal to the length of the digits.]

Time Complexity: O(n* 4^n) [at max 4 characters will be iterated.]
Space Complexity: O(n) [Recursion Stack Space] +  O(n* 4^n) [Storage space] where n=length of the digits

Solved: [14/03/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

from typing import List
class Solution:
    def letterCombinations(self, digits):
        result = []
        if not digits:
            return []

        phone_map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6': 'mno',
                     '7':'pqrs', '8':'tuv', '9':'wxyz'}

        def helper(index, temp):
            if index == len(digits):
                result.append(temp)
                return
            for letter in phone_map[digits[index]]:
                helper(index+1, temp+letter)
        helper(0, '')
        return result

if __name__ == "__main__":
    sol = Solution()
    assert sol.letterCombinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    assert sol.letterCombinations("2") == ["a", "b", "c"]
    print("✅ All tests passed!")