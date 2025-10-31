"""
Problem: [Valid Sudoku]
Link: https://leetcode.com/problems/valid-sudoku/
Difficulty: [Medium]
Topics: [Array, Default Dictionary, Hash table etc.]

Pattern: [Use a hash table to store the result row wise, column wise and square box wise, in case of Duplicacy return false]
Key Insight: []

Time Complexity: O(n^2)
Space Complexity: O(n)

Solved: [31/10/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐⭐⭐
"""

from typing import List, Set
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       rows = defaultdict(set)
       cols = defaultdict(set)
       square_box = defaultdict(set)

       for i in range(9):
           for j in range(9):
               if board[i][j] == '.':
                   continue
               if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in square_box[(i//3, j//3)]:
                   return False
               rows[i].add(board[i][j])
               cols[j].add(board[i][j])
               square_box[(i//3, j//3)].add(board[i][j])
       return True


if __name__ == "__main__":
    sol = Solution()
    assert sol.isValidSudoku([["1","2",".",".","3",".",".",".","."],
                             ["4",".",".","5",".",".",".",".","."],
                             [".","9","8",".",".",".",".",".","3"],
                             ["5",".",".",".","6",".",".",".","4"],
                             [".",".",".","8",".","3",".",".","5"],
                             ["7",".",".",".","2",".",".",".","6"],
                             [".",".",".",".",".",".","2",".","."],
                             [".",".",".","4","1","9",".",".","8"],
                             [".",".",".",".","8",".",".","7","9"]]) == True

    assert sol.isValidSudoku([["1","2",".",".","3",".",".",".","."],
                             ["4",".",".","5",".",".",".",".","."],
                             [".","9","1",".",".",".",".",".","3"],
                             ["5",".",".",".","6",".",".",".","4"],
                             [".",".",".","8",".","3",".",".","5"],
                             ["7",".",".",".","2",".",".",".","6"],
                             [".",".",".",".",".",".","2",".","."],
                             [".",".",".","4","1","9",".",".","8"],
                             [".",".",".",".","8",".",".","7","9"]]) == False

    print("✅ All tests passed!")