"""
Problem: kth Smallest Element in a BST
Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
Difficulty: [Medium]
Topics: [Binary Search Tree]

Pattern: [Depth First Search]
Key Insight:
•	In a Binary Search Tree, an inorder traversal visits nodes in ascending order.
•	To find the k-th smallest element, we perform an inorder DFS and count nodes as they are visited.
•	We traverse:
	1.	Left subtree (smaller values)
	2.	Current node
	3.	Right subtree (larger values)
•	A counter (count) is maintained as a class variable so its value persists across recursive calls.
•	Each time a node is visited (after left traversal), increment count.
•	When count == k, return the current node immediately.
•	Early termination ensures we do not traverse unnecessary parts of the tree once the answer is found.

Time Complexity
	•	Best case: O(h) — when the k-th smallest lies along the leftmost path
	•	Worst case: O(n) — when all nodes must be visited
Space Complexity
	•	O(h) — recursion stack, where h is the height of the tree

Solved: [02/02/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐⭐
"""

from utils import TreeNode
class Solution(object):
    def kthSmallest(self, root, k):
        self.count = 0
        def helper(node):
            if not node:
                return None
            left = helper(node.left)
            if left:
                return left
            self.count += 1
            if self.count == k:
                return node
            return helper(node.right)
        result = helper(root)
        return result.val

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.left.right = TreeNode(2)

    root.right = TreeNode(4)
    assert sol.kthSmallest(root, 1) == 1
    print("✅ All tests passed!")