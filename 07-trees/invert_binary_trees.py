"""
Problem: [Invert Binary Tree]
Link: https://leetcode.com/problems/invert-binary-tree/
Difficulty: [Easy]
Topics: [DFS, Binary Tree]

Pattern: [Depth First Search]
Key Insight:
* Traverse the tree using DFS and invert it by swapping left and right pointers at each node.

Time Complexity: O(n), where n is the number of nodes (each node is visited once).
Space Complexity: O(h) recursion stack, worst case O(n) for a skewed tree.

Solved: [26/01/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐⭐⭐
"""

from utils import TreeNode

class Solution(object):
    def invertTree(self, root):
        if not root:
            return
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    sol.invertTree(root)
    assert root.print_tree(root) == [2, 3, 1]
    print("✅ All tests passed!")