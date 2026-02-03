"""
Problem: Binary Tree Maximum Path sum
Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
Difficulty: [Hard]
Topics: [Binary Tree, Depth First Search]

Pattern: [Depth First Search]

Key Insight:
At each node, compute node.val + left_sum + right_sum to update the global maximum path, while returning node.val + max(left_sum, right_sum) to maintain a valid upward path.


Time Complexity: O(n) [all the nodes will be traversed]
Space Complexity: O(h) [recursive stack space]

Solved: [03/02/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

from utils import TreeNode
class Solution(object):
    def maxPathSum(self, root):
        self.max_sum = float('-inf')
        def dfs(root):
            if not root:
                return 0
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
            self.max_sum = max(self.max_sum, root.val + left + right)
            return root.val + max(left, right)
        dfs(root)
        return self.max_sum

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(-10)
    root.left = TreeNode(9)

    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    assert sol.maxPathSum(root) == 42
    print("✅ All tests passed!")