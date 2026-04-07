"""
Problem: [Intersection of Two Linked Lists]
Link: https://leetcode.com/problems/intersection-of-two-linked-lists/description/
Difficulty: [Easy]
Topics: [Linked List]

Pattern: [Two Pointers]
Key Insight: [Traverse both lists with two pointers; when one reaches the end, switch it to the other list’s head.
This equalizes path lengths and guarantees intersection detection.]

Time Complexity: O(len(headA) + len(headB))
Space Complexity: O(1)

Solved: [03/04/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""
from utils import Utility, ListNode
from typing import List


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        slow1, slow2 = headA, headB
        while slow1!=slow2:
            slow1 = headB if not slow1 else slow1.next
            slow2 = headA if not slow2 else slow2.next
        return slow1

if __name__ == "__main__":
    sol = Solution()
    common = ListNode(8)
    common.next = ListNode(4)
    common.next.next = ListNode(5)

    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = common

    headB = ListNode(5)
    headB.next = ListNode(6)
    headB.next.next = ListNode(1)
    headB.next.next.next = common

    assert sol.getIntersectionNode(headA, headB) == common
    print("✅ All tests passed!")