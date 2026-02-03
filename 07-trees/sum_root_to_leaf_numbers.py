"""
Problem: Sum Root to Leaf Numbers
Link: https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
Difficulty: [Medium]
Topics: [Binary Tree, Depth First Search]

Pattern: [Depth First Search]

Key Insight:
* To solve this problem, preorder traversal has to be used as root should be first.
* And as you follow the DFS path for preorder traversal, add root value in a temp string.
* Check for 2 base conditions - if root is none return
* If both left and right child are None then append the string in the resul list - which contain all the dfs
paths.
* After the function call, extract each element of the result list - convert it into int and add it into
a sum.
* Return the sum

Time Complexity: O(n)
Space Complexity: O(n) [for extra space] + O(h) [recursion stack space]

Solved: [03/02/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐⭐
"""

from utils import TreeNode
class Solution(object):
    def sumNumbers(self, root):
        result = []

        def dfs(root, temp):
            if not root:
                return
            if not root.left and not root.right:
                temp += (str(root.val))
                result.append(temp)
                return

            temp += str(root.val)
            dfs(root.left, temp)
            dfs(root.right, temp)

        dfs(root, '')
        ans = 0
        for s in result:
            ans += int(s)
        return ans

if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(4)
    root.left = TreeNode(9)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)
    root.right = TreeNode(0)

    assert sol.sumNumbers(root) == 1026
    print("✅ All tests passed!")