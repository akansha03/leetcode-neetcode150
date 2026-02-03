"""
Problem: Serialize and Deserialize Binary Tree
Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
Difficulty: [Hard]
Topics: [Binary Tree, Serialize String, Level Order Traversal]
Pattern: [Level Order Traversal]

Key Insight -
Serialization: Perform level-order traversal using a queue, enqueue None children as well, append values to a list using 'n' for nulls, then join the list into a
single string and return it.

Deserialization: Split the serialized string into a list, create the root from the first element and push it into a queue, then iterate through the
remaining elements assigning left and right children sequentially while de queuing parent nodes and enqueueing newly created child nodes.

Time Complexity: O(n)
Space Complexity: O(n) [for queue] + O(h) [recursive stack space]

Solved: [03/02/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

from collections import deque
from utils import TreeNode

class Codec:
    def serialize(self, root):
        if not root:
            return ''
        queue = deque([root])
        result = []

        while queue:
            node = queue.popleft()
            if not node:
                result.append('n ')
                continue
            result.append(str(node.val) + ' ')
            queue.append(node.left)
            queue.append(node.right)
        return ''.join(result)

    def deserialize(self, data):
        if not data:
            return None

        temp = data.split(' ')
        root = TreeNode(int(temp[0]))
        queue = deque([root])
        i = 1
        while i<len(temp)-1:
            node = queue.popleft()
            if temp[i] != 'n':
                node.left = TreeNode(int(temp[i]))
                queue.append(node.left)
            i += 1
            if temp[i] != 'n':
                node.right = TreeNode(int(temp[i]))
                queue.append(node.right)
            i+=1
        return root

if __name__ == "__main__":
    sol = Codec()
    root = TreeNode(1)
    root.left = TreeNode(2)

    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    data = sol.serialize(root)
    assert root.print_tree(sol.deserialize(data)) == [1,2,3,4,5]
    print("✅ All tests passed!")