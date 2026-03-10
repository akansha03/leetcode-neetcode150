"""
Problem: [N Queens]
Link: https://leetcode.com/problems/n-queens/description/
Difficulty: [Hard]
Topics: [List, Recursion, Backtracking]

Pattern: [Recursion + Backtracking + List + String]
Key Insight: [Queen attacks in 3 directions - vertically, left and right diagonal. Check that using is_safe method and
run loop for all rows and cols. If 'Q' is filled in one row, go to the next row recursively.]

Time Complexity: O(N!)
Space Complexity: O(n^2)

Solved: [10/03/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for _ in range(n)]
        result = []

        def is_safe(row, col):
            for i in range(n):
                if board[i][col] == 'Q':
                    return False

            i, j = row, col
            # check the left diagonal
            while i>=0 and j>=0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            i, j = row, col
            while i>=0 and j<n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True

        def backtrack(row):
            if row == n:
                result.append([''.join(r) for r in board])

            for col in range(n):
                if is_safe(row, col):
                    board[row][col] = 'Q'
                    backtrack(row+1)
                    board[row][col] = '.'
        backtrack(0)
        return result

if __name__ == "__main__":
    sol = Solution()
    assert sol.solveNQueens(4) == [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    print("✅ All tests passed!")