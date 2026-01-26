"""
Problem: Lowest Common Ancestor of a Binary Search Tree
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
Difficulty: [Medium]
Topics: [Binary Search Tree]

Pattern: [Depth First Search]
Key Insight:
* Store the current node as parent. If parent.val is greater than both p and q, the LCA lies in the
left subtree. If it is smaller than both, the LCA lies in the right subtree.
Otherwise, the current node is the lowest common ancestor.

Time Complexity: O(h) - average case and O(n) worst case if skewed tree
Space Complexity: O(h) - recursive stack

Solved: [26/01/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""
from utils import TreeNode

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None
        parent = root.val
        if parent>p.val and parent>q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif parent<p.val and parent<q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(6)
    root.left = TreeNode(2)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)

    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    root.right = TreeNode(8)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    p = TreeNode(2)
    q = TreeNode(8)
    assert root.print_tree(sol.lowestCommonAncestor(root, p, q))[0] == 6
    print("✅ All tests passed!")