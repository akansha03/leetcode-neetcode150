"""
Problem: Same Tree
Link: https://leetcode.com/problems/same-tree/description/
Difficulty: [Easy]
Topics: [Binary Tree]

Pattern: [Depth First Search]
Key Insight:
* Perform DFS on both trees simultaneously.
* If both nodes are None, return True; if one is None or their values differ, return False.
* Recursively compare left and right subtrees.

Time Complexity: O(n), each node is visited once
Space Complexity: O(h), recursion stack up to the height of the tree

Solved: [26/01/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐⭐⭐
"""

from utils import TreeNode
class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) or self.isSameTree(p.right, q.right)

if __name__ == "__main__":
    sol = Solution()
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    assert sol.isSameTree(p, q) == True
    print("✅ All tests passed!")