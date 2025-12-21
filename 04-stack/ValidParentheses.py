"""
Problem: [Valid Parentheses]
Link: https://leetcode.com/problems/valid-parentheses/
Difficulty: [Easy]
Topics: [Array, Stack]

Pattern: [Stacks]

Key Insight:

* To figure out whether the expression is valid or not, stack has to be used.

* All the opening braces are put into the stack and if a closing brace comes then check the top element
 if there is a match of braces.

* If yes, then  pop the last element - else no need to go further that means it's imbalanced - pop the
element out.

* At last check if the stack is empty or not. should be empty - shows a balanced expression

Time Complexity: O(n)

Space Complexity: O(n)

Solved: [6/12/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        stack = []
        for c in s:
            if c == '[' or c == '(' or c == '{':
                stack.append(c)
            else:
                if not stack:
                    return False
                elif c == ']' and stack[-1] == '[' or c == ')' and stack[-1] == '(' or c == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        return stack == []

if __name__ == "__main__":
    sol = Solution()
    assert sol.isValid("()") == True
    assert sol.isValid("()[]{}") == True
    assert sol.isValid("(]") == False
    assert sol.isValid("([])") == True
    assert sol.isValid("([)]") == False
    print("✅ All tests passed!")