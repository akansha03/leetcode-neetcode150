"""
Problem: [Copy List with Random Pointer]
Link: https://leetcode.com/problems/copy-list-with-random-pointer/description/
Difficulty: [Medium]
Topics: [Hash Table, Linked List]

Pattern: [Deep copy, Hash table (store copy of original with copied pointer)]
Key Insight:
* Create a deep copy of the list and return the head of the new node.
* Instinct that comes to mind is to use recursion and assign all the elements of the original list
to the new list.
* To do so, I will be using a map, which stores the reference of original node as the key and reference of
new_node as value.

Time Complexity: O(n)
Space Complexity: O(n)

Solved: [29/12/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

from typing import Optional
from utils import Utility

class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        clone_map = {}
        def copyList(node):
            if not node:
                return None
            if node in clone_map:
                return clone_map[node]

            new_node = Node(node.val)
            clone_map[node] = new_node

            new_node.next = copyList(node.next)
            new_node.random = copyList(node.random)
            return new_node
        return copyList(head)
if __name__ == "__main__":

    head = Node(7)
    head.next = Node(13)
    head.next.next = Node(11)
    head.next.next.next = Node(10)
    head.next.next.next.next = Node(1)

    sol = Solution()
    util = Utility()
    assert util.to_list(sol.copyRandomList(head)) == [7,13,11,10,1]
    print("✅ All tests passed!")