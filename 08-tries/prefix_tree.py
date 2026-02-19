"""
Problem: [Implement Trie (Prefix Tree)]
Link: https://leetcode.com/problems/implement-trie-prefix-tree/description/
Difficulty: [Medium]
Topics: [Trie]

Pattern: [Building a prefix tree using characters of a word]

Key Insight:
* Trie stores strings in a tree structure where each node represents a character, enabling efficient prefix-based search.

* Define a TrieNode class with a children dictionary to store character mappings and an isLeaf (or isEnd) flag to indicate
the end of a word.

* For insertion, start from the root and iterate through each character of the word. If the character is not present in
node.children, create a new TrieNode; otherwise, move to the existing child node. Mark the final node as isLeaf = True.

* For full word search, start from the root and traverse character by character. If any character is missing in children,
return False; after full traversal, return node.isLeaf to ensure it is a complete word.

* For prefix search, traverse the Trie using the prefix characters. If any character is missing, return False;
if the prefix is fully traversed, return True.

Time Complexity: O(len(word)) [insert] + O(len(word)) + O(len(prefix))
Space Complexity: O(total number of words inserted)

Solved: [11/02/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLeaf = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        node.isLeaf = True

    def search(self, word: str) -> bool:
        node = self.root
        for w in word:
            if w not in node.children:
                return False
            node = node.children[w]
        return node.isLeaf

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for p in prefix:
            if p not in node.children:
                return False
            node = node.children[p]
        return True

if __name__ == "__main__":
    trie = Trie()
    op = ["insert", "search", "search", "startsWith", "insert", "search"]
    inputs = ["apple", "apple", "app", "app", "app", "app"]
    output = [None, True, False, True, None, True]

    for i,choice in enumerate(op):
        if choice == "insert":
            trie.insert(inputs[i])
            break
        elif choice == "search":
            assert trie.search(inputs[i]) == output[i]
            break
        else:
            assert trie.startsWith(inputs[i]) == output[i]
    print("✅ All tests passed!")