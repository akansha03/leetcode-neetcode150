"""
Problem: Validate Binary Search Tree
Link: https://leetcode.com/problems/validate-binary-search-tree/
Difficulty: Medium
Topics: Binary Search Tree

Pattern: [Depth First Search]
Key Insight:

A Binary Search Tree has the property that an inorder traversal produces values in strictly increasing order.
A brute-force approach would be to store the inorder traversal in an array and then check if the array is sorted.
To optimize space, we avoid storing the entire traversal.
Instead, we track only the previously visited node value (prev) during the inorder traversal.
During DFS:
	Recursively traverse the left subtree.
	Compare the current node’s value with prev.
	If prev ≥ current node value, the BST property is violated.
	Update prev to the current node’s value.
	Recursively traverse the right subtree.
	If all nodes satisfy the increasing order condition, the tree is a valid BST.

Time Complexity
	•	O(n) — every node is visited exactly once.
Space Complexity
	•	O(h) — recursion stack, where h is the height of the tree
	•	Worst case (skewed tree): O(n)
	•	Best case (balanced tree): O(log n)

Solved: [02/02/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐⭐
"""
from utils import TreeNode

class Solution(object):
    def isValidBST(self, root):
        self.prev = None
        def dfs(root):
            if not root:
                return True
            left = dfs(root.left)
            if not left:
                return False
            if self.prev is not None and self.prev >= root.val:
                return False
            self.prev = root.val
            return dfs(root.right)
        return dfs(root)

if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)

    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    assert sol.isValidBST(root) == False
    print("✅ All tests passed!")