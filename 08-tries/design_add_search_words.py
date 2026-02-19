"""
Problem: [Design Add and Search Words Data Structure]
Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/
Difficulty: [Medium]
Topics: [Trie, Binary Tree]

Pattern: [Trie, DFS]

Key Insight:

* addWord is similar to standard Trie insertion: start from the root and insert each character of the word into the Trie.
* search differs from normal Trie search because the character '.' can represent any letter. To handle this wildcard, use DFS to explore all possible child nodes when '.' is encountered.
* Base condition: when the index reaches the length of the word, return whether node.isLeaf (or isEnd) is True.

Time Complexity: O(len(word)) - addWord + O(len(word)) - search
Space Complexity: O(len(word)) - recursion stack space

Solved: [12/02/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐⭐
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLeaf = False

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.isLeaf = True        
        
    def search(self, word):
        def dfs(node, index):
            if index == len(word):
                return node.isLeaf
            if word[index] == '.':
                return any(dfs(children, index+1) for children in node.chidren.values())
            if word[index] in node.chidren:
                return dfs(node.chidren[word[index]], index+1)
            return False

        return dfs(self.root, 0)

if __name__ == "__main__":
    sol = WordDictionary()
    ops = ["addWord","addWord","addWord","search","search","search","search"]
    inputs = ["bad", "dad", "mad", "pad", "bad" , ".ad", "b.."]
    output = [None, None, None, False, True, True, True]

    for i, op in enumerate(ops):
        if op == "addWord":
            sol.addWord(inputs[i])
            break
        else:
            assert sol.search(inputs[i]) == output[i]
    print("✅ All tests passed!")