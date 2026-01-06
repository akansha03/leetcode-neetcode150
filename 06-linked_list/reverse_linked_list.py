"""
Problem: [Reverse Linked List]
Link: https://leetcode.com/problems/reverse-linked-list/description/
Difficulty: [Easy]
Topics: [Linked List]

Pattern: [Current and Previous Pointer]
Key Insight:
* To achieve this we'll take two pointers, prev and current.
* Current will be pointing to the head and prev to None.
* Traverse through current:
    - Get the next value and store it in a temp,i.e., current.next
        1->2>3->4->None
    - temp will have value 2, then point current.next to prev, 1->None
    - assign current to the prev node
    - and assign temp to current, i.e., current = 2
* Repeat this util current is None
* Return prev node as it will be pointing to 4,i.e., 4->3->2->1

Time Complexity: O(n)
Space Complexity: O(1)

Solved: [26/12/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""
from utils import Utility, ListNode


class Solution(object):
    def reverseList(self, head):
        if not head:
            return None

        prev, current = None, head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2, None)
    sol = Solution()
    util = Utility()
    assert util.to_list(sol.reverseList(head)) == [2,1]
    print("✅ All tests passed!")