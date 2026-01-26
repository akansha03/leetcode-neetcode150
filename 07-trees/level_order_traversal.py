"""
Problem: [Binary Tree Level Order Traversal]
Link: https://leetcode.com/problems/binary-tree-level-order-traversal/description/
Difficulty: [Medium]
Topics: [Binary Tree, Breadth First Search]

Pattern: Breadth First Search
Key Insight:
Use a queue to perform level-order traversal. For each level, process all nodes currently in the queue,
collect their values in a temporary list, and append it to the final result while enqueuing left and right children.

Time Complexity: O(n), each node is visited once
Space Complexity: O(n), queue can hold up to one full level of nodes

Solved: [26/01/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐⭐⭐
"""

from utils import TreeNode
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        queue = deque([root])
        result = []

        while queue:
            size = len(queue)
            temp = []
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                temp.append(node.val)
            result.append(temp)
        return result

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert sol.levelOrder(root) == [[3],[9,20],[15,7]]
    print("✅ All tests passed!")