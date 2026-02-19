"""
Problem: [Word Search I]
Link: https://leetcode.com/problems/word-search/description/
Difficulty: [Medium]
Topics: [DFS, Backtracking, matrix, DFS on matrix]

Pattern: [Backtracking, DFS]
Key Insight:

Use DFS with backtracking to explore all possible paths in the matrix using the four directions: (-1,0), (1,0), (0,-1), (0,1).
Check boundary conditions properly (i < 0, i >= m, j < 0, j >= n) to avoid invalid indices.
Compare the current cell with word[index]. If it doesn’t match, return False.
Mark the current cell as visited (for example, set it to '#') so it is not reused in the same path.
After exploring all directions, restore the original value (backtrack) so it can be used in other paths.

Time Complexity: O(m*n*4^l)
[If the word matches then all four directions will be explored - mostly 3 as 1 would be already visited in most scenarios]

Space Complexity: O(l)
[recursive space - as length of the word]

Solved: [16/02/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get the length of row and column
        m, n = len(board), len(board[0])

        def dfs(i, j, index):
            if index == len(word):
                return True
            if i<0 or i>=m or j<0 or j>=n or board[i][j] != word[index]:
                return False

            temp = board[i][j]
            board[i][j] = '#'
            found = dfs(i-1,j,index+1) or dfs(i+1,j,index+1) or dfs(i,j-1,index+1) or dfs(i,j+1, index+1)
            board[i][j] = temp
            return found

        for i in range(m):
            for j in range(n):
                if dfs(i,j, 0):
                    return True
        return False        

if __name__ == "__main__":
    sol = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "SEE"
    assert sol.exist(board, word) == True
    board_1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word_1 = "ABCB"
    assert sol.exist(board_1, word_1) == False
    print("✅ All tests passed!")