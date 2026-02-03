"""
Problem: Count Good Nodes in Binary Tree
Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
Difficulty: [Medium]
Topics: [Binary Tree]

Pattern: [DFS, Binary Tree]

Key Insight:
• Use DFS because the decision of whether a node is “good” depends on the path from the root to that node.
• Define a helper function that takes the current node and the maximum value seen so far on that path.
• At each node, compare node.val with the path maximum; if it is greater than or equal, count it as a good node.
• Update the path maximum using max(current_max, node.val) and pass it to recursive calls.
• Recursively apply the same logic to the left and right subtrees and accumulate the count.

Time Complexity: O(n) - all the nodes will be touched
Space Complexity: O(h) - recursive space

Solved: [29/01/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐⭐
"""
from utils import TreeNode

class Solution(object):
    def goodNodes(self, root):

        def dfs(root, val):
            if not root:
                return 0
            good = 1 if root.val>=val else 0
            val = max(val, root.val)

            return good + dfs(root.left, val) + dfs(root.right, val)
        return dfs(root, root.val)

if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(3)
    root.left = TreeNode(1)
    root.left.left = TreeNode(3)

    root.right = TreeNode(4)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)
    assert sol.goodNodes(root) == 4
    print("✅ All tests passed!")