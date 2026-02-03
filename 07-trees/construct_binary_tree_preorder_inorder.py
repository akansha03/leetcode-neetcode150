"""
Problem: Construct Binary Tree from Preorder and Inorder Traversal
Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
Difficulty: [Medium]
Topics: [Binary Tree]

Pattern: [Hash Table, Divide and Conquer, Binary Tree]
Key Insights:
* Store the elements of inorder in a map along with the indexes so that this could be used for left and right
index calculation.
* As Inorder will give the index of the root node, left and right subtree will give the possible indexes.
* Create a helper function with p_start, p_end, i_start, i_end indexes
* Steps:
    - extract the root node from preorder list as it will be preorder[p_start]
    - Get the root index from the inorder map and get the left index from root_index-i_start
    - recursive function for root.left stating the index from where left subtree will start and end
        * p_start+1 to p_start+left_index
        * i_start to root_index
    - recursive function for root.right stating the index from where right subtree will start and end
        * p_start+left_index+1 to p_end
        * root_index+1 to i_end
    - return root

Time Complexity: O(n)
Space Complexity: O(n)

Solved: [02/02/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""
from utils import TreeNode
class Solution(object):
    def helper(self, p_start, p_end, i_start, i_end, result, preorder):
        if p_start>p_end or i_start>i_end:
            return None

        root = TreeNode(preorder[p_start])
        root_index = result[preorder[p_start]]
        left_index = root_index-i_start

        root.left = self.helper(p_start+1, p_start+left_index, i_start, root_index, result, preorder)
        root.right = self.helper(p_start+left_index+1, p_end, root_index+1, i_end, result, preorder)
        return root

    def buildTree(self, preorder, inorder):
        # form an inorder map
        result = {}
        for i,num in enumerate(inorder):
            result[num] = i
        size = len(inorder)
        return self.helper(0, size-1, 0, size-1, result, preorder)

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(-1)
    assert root.print_tree(sol.buildTree([1,2,3,4], [2,1,3,4])) == [1,2,3,4]
    print("✅ All tests passed!")