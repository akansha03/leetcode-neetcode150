"""
Problem: [Generate Parentheses]
Link: https://leetcode.com/problems/generate-parentheses/description/
Difficulty: [Medium]
Topics: [List, Recursion, Backtracking]

Pattern: [Recursion + Backtracking + Generation code]
Key Insight: [Two variables are taken to keep track of open, close brackets and an empty string. Idea is to append the
opening braces till n, and then closing braces with condition that close braces are less than open - so that the string
is valid i.e, number of opening braces are equal to closing ones.]

Time Complexity: O(4^n/sqrt(n))
Space Complexity: O(n) [recursion space]

Solved: [07/03/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

class Solution(object):
    def generateParenthesis(self, n):
        result = []
        def helper(open, close, s):
            if len(s) == 2*n:
                result.append(s)
                return
            if open<n:
                helper(open+1, close, s+'(')
            if close<open:
                helper(open, close+1, s+')')
        helper(0, 0, '')
        return result

if __name__ == "__main__":
    sol = Solution()
    assert sol.generateParenthesis(3) == ["((()))","(()())","(())()","()(())","()()()"]
    assert sol.generateParenthesis(1) == ["()"]
    print("✅ All tests passed!")