"""
Problem: Evaluate Reverse Polish Notation
Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/
Difficulty: [Medium]
Topics: [Array, Stack, String]

Pattern: Add the numbers in the stack and pop top 2 elements to perform an operation.

Key Insight:

* Iterate the token, when token is not among the arithmetic operators - append it to the stack.

* If not, then pop the top 2 elements, and perform respective operations and store the result back
into the stack, so that the new operation could be performed on the last output element

Time Complexity: O(n)
Space Complexity: O(n)

Solved: [07/12/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ['+', '*', '-', '/']:
                stack.append(int(token))
            else:
                val1, val2 = stack.pop(), stack.pop()
                if token == '+':
                    output = val1 + val2
                elif token == '-':
                    output = val2 - val1
                elif token == '*':
                    output = val1 * val2
                else:
                    output = int(val2/val1)
                stack.append(output)
        return stack[-1]

if __name__ == "__main__":
    sol = Solution()
    assert sol.evalRPN(["2","1","+","3","*"]) == 9
    assert sol.evalRPN(["4","13","5","/","+"]) == 6
    assert sol.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22
    print("✅ All tests passed!")