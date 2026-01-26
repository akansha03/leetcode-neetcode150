"""
Problem: Subtree of Another Tree
Link: https://leetcode.com/problems/subtree-of-another-tree/description/
Difficulty: [Easy]
Topics: [Binary Tree, Serialize Binary Tree]

Pattern: Depth First Search
Key Insight:
* Serialize both the tree and the subtree using DFS (including null markers) and check whether the serialized
subtree string is a substring of the serialized tree string.

Time Complexity: O(n), serialization visits each node once
Space Complexity: O(n), space used to store the serialized strings

Solved: [26/01/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐⭐⭐
"""

from utils import TreeNode

class Solution(object):
    def isSubtree(self, root, subRoot):
        def helper(root):
            if not root:
                return 'n'
            return '#' + str(root.val) + helper(root.left) + helper(root.right)
        p1 = helper(root)
        p2 = helper(subRoot)
        return p2 in p1

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)

    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)

    subroot = TreeNode(4)
    subroot.left = TreeNode(1)
    subroot.right = TreeNode(2)
    assert sol.isSubtree(root, subroot) == True
    print("✅ All tests passed!")