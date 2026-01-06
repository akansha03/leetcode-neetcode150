"""
Problem: [Reverse Nodes in k group]
Link: https://leetcode.com/problems/reverse-nodes-in-k-group/
Difficulty: [Hard]
Topics: [List, Linked List]

Pattern: [Linked List, Indexing]
Key Insight:
* Brute Force Solution solved so far, I have converted the singly linked list into a list.
* Traversed the list from index = 0 to n, inside that there is a start and end, i.e., index, index+k-1
* swap the start and end index elements, to reverse a portion.
* After that, update the index to index+k which in turn will become the start index and then repeat the same for rest of
the list elements.

# Optimal Approach - Iterative solution

* In my own words, Intuitively I was able to figure out that there will be something like start, middle[which will be reversed]
and last.
* I faced issue with how to link them and while reversing not taking prev as None - this was a new for me.
* Idea is to figure out the kth node till where the reversal will happen, then
* start will be the pointer, i.e., which will point to the last node of first part of the list.
* so if the first k nodes are getting reversed then -1 th node will be the start else in below example
start will be the 2. 1->2  3->4->5
* first get the kth node, so the reversal will happen from start.next and kth node
* store last = kthnode.next
* Once reversal is completed, now is a very important part - linking starts
* basically now update the start pointer to move to last node of the reversed list and start.next = kthnode will do the
linking part(this took some time to figure out)


For Brute Force Solution
- Time Complexity: O(n^2)
- Space Complexity: O(n)

For Optimal Solution:
- Time Complexity : O(n)
- Space Complexity : O(1)

Solved: [03/01/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

from typing import Optional
from utils import Utility, ListNode

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''Following is the brute force solution'''
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next

        index, n = 0, len(result)
        while index<n:
            start, end = index, index+k-1
            while start < end < n:
                result[start], result[end] = result[end], result[start]
                start += 1
                end -= 1
            index = index+k

        head = ListNode(-1)
        temp = head
        for r in result:
            temp.next = ListNode(r)
            temp = temp.next
        return head.next


    def reverse_k_nodes_iterative(self, head, k):
        dummy = ListNode(0, head)
        start = dummy

        while True:
            kthNode = self.getKthNode(start, k)
            if not kthNode:
                break
            last = kthNode.next

            # Start the reversal
            prev, current = kthNode.next, start.next
            while current != last:
                temp = current.next
                current.next = prev
                prev = current
                current = temp

            # Start the linking process - so first half of the list already reversed or at a beginning should point to the
            # reversed list
            temp = start.next
            start.next = kthNode
            start = temp
        return dummy.next

    def getKthNode(self, current, k):
        while current and k>0:
            current = current.next
            k -= 1
        return current

if __name__ == "__main__":
    inputs = [1,2,3,4,5,6]
    head = ListNode(-1)
    temp = head
    for i in inputs:
        temp.next = ListNode(i)
        temp = temp.next

    util = Utility()
    sol = Solution()
   # assert util.to_list(sol.reverseKGroup(head.next, 3)) == [3,2,1,6,5,4]
    assert util.to_list(sol.reverse_k_nodes_iterative(head.next, 3)) ==  [3,2,1,6,5,4]
    print("✅ All tests passed!")