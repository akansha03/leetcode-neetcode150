"""
Problem: [Remove Node From End of Linked List]
Link: https://neetcode.io/problems/remove-node-from-end-of-linked-list/question?list=neetcode150
Difficulty: [Medium]
Topics: [Linked List, Two Pointers]

Pattern: [Two Pointers, Linked List - slow and fast]
Key Insight:
* First solution that comes to mind is to calculate the length of the list and get the target node by subtracting
len(list)-n.
* Take two pointers and navigate till the target node and use prev node to point to current.next.i.e., prev.next = current.next
* To optimise the above code and remove the node in the single traversal - use slow and fast pointer.
* Take temp dummy node, point it next to head and assign slow and next pointer to temp.
* run a loop and move ahead the fast pointer by n
* move slow and fast pointer til fast.next is none and slow will be pointing to the node before the target node to be deleted.
* now simply do, slow.next = slow.next.next
* return temp.next

Time Complexity: O(n)
Space Complexity: O(1)

Solved: [28/12/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""
from utils import Utility, ListNode
from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        size, current = 0, head
        while current:
            size += 1
            current = current.next
        i, target = 0, size-n
        prev, current = None, head
        while i<target:
            prev = current
            current = current.next
            i += 1
        if target == 0:
            return current.next
        prev.next = current.next
        return head

    def single_traverse_remove_Nth_From_End(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        temp = ListNode(-1)
        temp.next = head
        slow = fast = temp
        # Make fast get ahead by n
        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return temp.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    head1 = ListNode(1)
    head1.next = ListNode(2)

    head2 = ListNode(1)
    sol = Solution()
    util = Utility()
    assert util.to_list(sol.single_traverse_remove_Nth_From_End(head, 2)) == [1,2,3,5]
    assert util.to_list(sol.single_traverse_remove_Nth_From_End(head1, 1)) == [1]
    assert util.to_list(sol.single_traverse_remove_Nth_From_End(head2, 1)) == []
    print("✅ All tests passed!")