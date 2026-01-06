"""
Problem: [Merge Two Sorted Lists]
Link: https://leetcode.com/problems/merge-two-sorted-lists/
Difficulty: [Medium]
Topics: [Linked List, Merge Sort]

Pattern: [Merge Sort]
Key Insight:
* This technique is driven from the concept of merge sort where we compare which one of the two lists has the smaller element.
* To achieve this, we will be taking a dummy node with value as -1 and smaller node will be appended using next.
* Keep on traversing the dummy node to the next.
* In case the length of the lists are uneven or one of them is finished, check at the end if they are None or not.
* Add the remaining elements directly to the next of the dummy pointer

Time Complexity: O(n+m)
Space Complexity: O(1)

Solved: [26/12/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""
from utils import Utility, ListNode

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        result = ListNode(-1)
        temp = result
        while list1 and list2:
            if list1.val<=list2.val:
                result.next = list1
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next
            result = result.next
        while list1:
            result.next = list1
            list1 = list1.next
            result = result.next
        while list2:
            result.next = list2
            list2 = list2.next
            result = result.next
        return temp.next

if __name__ == "__main__":
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(4)

    head2 = ListNode(1)
    head2.next = ListNode(3)
    head2.next.next = ListNode(4)

    util = Utility()
    sol = Solution()
    assert util.to_list(sol.mergeTwoLists(head1, head2)) == [1,1,2,3,4,4]
    print("✅ All tests passed!")