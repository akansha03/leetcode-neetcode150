"""
Problem: [Add Two Numbers]
Link: https://leetcode.com/problems/add-two-numbers/
Difficulty: [Medium]
Topics: [Linked List, Carry forward, Sum of 2 linked list]

Pattern: [Linked List, Carry]
Key Insight:

* Intuition that came to me is that there are two possibilities - either there is a carry or there is not.
* So maintaining the variable, named carry.
* Traverse both the linked list with condition, i.e., l1 and l2, add the values from both the nodes along with carry
to get the sum.
* Next calculate the sum and carry, if sum is more than 9 then carry will be forwarded.
* Calculate the carry by sum//10 and calculate the addition by sum%10
* Use the sum to create a new node and attach it to a dummy node for navigation.
* We for sure know that linked list could be of different lengths so navigate through both of them to check if there are
remaining nodes - add them directly to the result list and perform the same operation with list2.
* At the end, check for carry - if there is an outstanding carry, carry>0 - create a node of it and append it at the end.

Time Complexity: O(len(l1) + len(l2)) => O(m+n)
Space Complexity: O(1)

Solved: [01/01/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""
from typing import Optional
from utils import ListNode, Utility

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1

        temp = ListNode(-1)
        result = temp
        carry = 0
        while l1 and l2:
            add = carry + l1.val + l2.val
            carry = add//10
            add = add%10
            result.next = ListNode(add)
            l1, l2, result = l1.next, l2.next, result.next

        while l1:
            add = carry + l1.val
            carry = add//10
            add = add%10
            result.next = ListNode(add)
            l1, result = l1.next, result.next

        while l2:
            add = carry + l2.val
            carry = add//10
            add = add%10
            result.next = ListNode(add)
            l2, result = l2.next, result.next

        if carry > 0:
            result.next = ListNode(carry)
        return temp.next

if __name__ == "__main__":

    sol = Solution()
    l1 = ListNode(9)
    l1.next = ListNode(9)
    l1.next.next = ListNode(9)
    l1.next.next.next = ListNode(9)
    l1.next.next.next.next = ListNode(9)
    l1.next.next.next.next.next = ListNode(9)
    l1.next.next.next.next.next.next = ListNode(9)

    l2 = ListNode(9)
    l2.next = ListNode(9)
    l2.next.next = ListNode(9)
    l2.next.next.next = ListNode(9)

    head = sol.addTwoNumbers(l1, l2)
    util = Utility()
    assert util.to_list(head) == [8,9,9,9,0,0,0,1]
    print("✅ All tests passed!")