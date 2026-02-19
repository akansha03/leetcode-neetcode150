"""
Problem: [ Word Search II]
Link: https://leetcode.com/problems/word-search-ii/description/
Difficulty: [Hard]
Topics: [Trie, List, Matrix, Recursion, Backtracking]

Pattern: [Trie]
Key Insight:
[An extension of Word Search I, but here return the words found in the matrix. Form a Trie with a list of
words and then use DFS to search the words in the matrix.]

Time Complexity: O(?)
Space Complexity: O(?)

Solved: [12/02/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""
from typing import List
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLeaf = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.isLeaf = True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        m, n = len(board), len(board[0])
        trie = Solution()

        for word in words:
            trie.insert(word)

        result = []
        def dfs(i, j, node, word):
            if i<0 or i>=m or j<0 or j>=n:
                return

            temp = board[i][j]
            if board[i][j] == '#' or temp not in node.children:
                return
            node = node.children[temp]
            if node.isLeaf:
                result.append(word+temp)
                node.isLeaf = False

            board[i][j] = '#'
            dfs(i-1, j, node, word+temp)
            dfs(i+1, j, node, word+temp)
            dfs(i, j-1, node, word+temp)
            dfs(i, j+1, node, word+temp)
            board[i][j] = temp

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie.root, '')
        return result


if __name__ == "__main__":
    sol = Solution()
    boards = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath", "pea", "eat", "rain"]

    board_1 = [["a", "b"], ["c", "d"]]
    words_1 = ["abcb"]

    assert sol.findWords(boards, words) == ["oath","eat"]
    assert sol.findWords(board_1, words_1) == []
    print("✅ All tests passed!")