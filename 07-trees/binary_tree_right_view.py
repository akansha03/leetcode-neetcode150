"""
Problem: Binary Tree Right Side View
Link: https://leetcode.com/problems/binary-tree-right-side-view/description/
Difficulty: [Medium]
Topics: [Binary Tree]

Pattern: [Breadth First Search]

Key Insight:
* This problem is an extension of level order traversal, when iterating the queue - use an index and
once index == size-1, store that particular node value in the result list.

Time Complexity: O(n)
Space Complexity: O(n)

Solved: [29/01/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐⭐⭐
"""
from utils import TreeNode
from collections import deque

class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            size = len(queue)
            last = None
            for _ in range(size):
                node = queue.popleft()
                last = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if last:
                result.append(last.val)
        return result

    # this is just for revision purposes - last node and index methods both work fine

    def rightSideViewIndex(self, root):
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            size = len(queue)
            for index in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if index == size-1:
                    result.append(node.val)
        return result

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)

    root.right = TreeNode(3)
    root.right.right = TreeNode(4)

    assert sol.rightSideView(root) == [1,3,4]
    assert sol.rightSideViewIndex(root) == [1, 3, 4]
    print("✅ All tests passed!")