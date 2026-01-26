"""
Problem: Maximum Depth of Binary Tree
Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
Difficulty: [Easy]
Topics: [Binary Tree]

Pattern: Depth First Search

Key Insight:
* Recursively compute the height of left and right subtrees and return 1 + max(leftHeight, rightHeight).

Time Complexity: O(n), where n is the number of nodes (each node is visited once).
Space Complexity: O(h), due to recursion stack, where h is the height of the tree.

Solved: [26/01/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐⭐⭐
"""

from utils import TreeNode
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)

    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    assert sol.maxDepth(root) == 3
    print("✅ All tests passed!")