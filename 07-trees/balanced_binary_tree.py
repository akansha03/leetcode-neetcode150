"""
Problem: Balanced Binary Tree
Link: https://leetcode.com/problems/balanced-binary-tree/description/
Difficulty: [Easy]
Topics: [Binary Tree]

Pattern: Depth First Search
Key Insight:
* For balanced binary tree, traverse and get the heights of the left and right subtree.
* Calculate the class level variable flag at every level by getting the abs(lh-rh) and it shouldn't be more than 1

Time Complexity: O(n)
Space Complexity: O(h)

Solved: [26/01/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐⭐⭐
"""

from utils import TreeNode

class Solution(object):
    def isBalanced(self, root):
        self.flag = True
        def helper(root):
            if not root:
                return 0
            lh = helper(root.left)
            rh = helper(root.right)
            if abs(lh-rh)>1:
                self.flag = False
            return 1 + max(lh, rh)
        helper(root)
        return self.flag

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(3)

    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(4)

    root.right = TreeNode(2)
    assert sol.isBalanced(root) == False
    print("✅ All tests passed!")