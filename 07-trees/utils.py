
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def print_tree(self, root):
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

