"""
Problem: [Reorder Linked List]
Link: https://leetcode.com/problems/reorder-list/description/
Difficulty: [Medium]
Topics: [Linked List, Slow and Fast Pointer]

Pattern: [Slow and Fast Pointer]
Key Insight:
* First thought that came into my mind while solving this problem is that why not reverse the list and then
point the nodes alternatively.
* But if I reverse the whole list then the original list order would be impacted, so instead of reversing the entire list,
why not reverse just the half.
* To do so, I have to know the index from where the list reversal will happen and to achieve this - slow and fast
pointer technique works really well.
* After getting the list node pointed by the slow pointer, I know that this is the last node of list1 and slow.next
is the node from where the reversal will start.
* Reverse the list from slow.next to None
* One Key point to remember here is - list goes like this : head ->...-> slow -> second. slow pointer is the key between
list1 and list2, this has to be made null, otherwise break will not happen and on forward traversal - linked list loop
will be formed.
* Post this take first and head and second as prev, start the iteration of taking the node from first -> pointing it
to the second, point second.next to first.next and keep on doing until the reversed list is None.[As reversed list will
exhaust first most likely then we'll take this as a counter.]

Time Complexity: O(n)
Space Complexity: O(1)

Solved: [27/12/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""
from utils import Utility, ListNode
from typing import Optional
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        prev = slow.next = None
        while second:
            temp = second.next
            second.next = prev

            prev = second
            second = temp
        first, second = head, prev
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    sol = Solution()
    sol.reorderList(head)
    util = Utility()
    assert util.to_list(head) == [1,4,2,3]
    print("✅ All tests passed!")