"""
Problem: Diameter of Binary Tree
Link: https://leetcode.com/problems/diameter-of-binary-tree/description/
Difficulty: [Easy]
Topics: [Binary Tree]

Pattern: Depth First Search
Key Insight:
* Use DFS to compute subtree heights; at each node, update a class-level diameter using leftHeight + rightHeight.

Time Complexity: O(n), each node is processed once
Space Complexity: O(h), recursion stack proportional to tree height

Solved: [26/01/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

from utils import TreeNode
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        def helper(root):
            if not root:
                return 0
            lh = helper(root.left)
            rh = helper(root.right)
            self.diameter = max(self.diameter, lh+rh)
            return 1 + max(lh, rh)
        helper(root)
        return self.diameter

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    assert sol.diameterOfBinaryTree(root) == 3
    print("✅ All tests passed!")