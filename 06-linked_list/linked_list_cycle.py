"""
Problem: [NAME]
Link: https://leetcode.com/problems/linked-list-cycle/description/
Difficulty: [Easy]
Topics: [Linked List, Slow and Fast Pointer]

Pattern: [Slow and Fast Pointer, Linked List]
Key Insight:
* This solution is not that intuitive and has to be revised continuously.
* Take two pointers - slow and fast, pointing to head.
* slow will move forward one at a time and fast will be 2 times ahead.
* Idea is if there is a cycle the slow and fast pointer will point at a same node at some point.
* Check for the condition, where slow == fast, if yes then return True
* If there is no cycle then fast pointer will reach the end of the list and then a false will be returned

Time Complexity: O(n)
Space Complexity: O(1)

Solved: [26/12/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""
from utils import ListNode

class Solution(object):
    def hasCycle(self, head):
        if not head:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

if __name__ == "__main__":
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    sol = Solution()
    assert sol.hasCycle(head1) == False

    n1 = ListNode(1)
    n1.next = ListNode(2)
    n1.next.next = n1
    assert sol.hasCycle(n1) == True
    print("✅ All tests passed!")