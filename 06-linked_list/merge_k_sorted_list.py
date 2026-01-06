"""
Problem: [Merge k Sorted list]
Link: https://leetcode.com/problems/merge-k-sorted-lists/description/
Difficulty: [Hard]
Topics: [Linked List, Merge Sort]

Pattern: [Merge Sort, Handling k lists]

Key Insight:
* I will be using the merge 2 sorted list function here - I won't go in details.
* Now the main agenda is to merge the k lists into 1.
* Run a main loop where n,i.e., length of the list is greater than 1
* To achieve this - get the length of the list and use 2 variables - i and j.
* i = 0 and j = size-1, lists at both these positions will be merged into lists[i] and returned - do i++ and j--
* At some point i==j then break
* Update the value of n to be j, Loop all this again where i = 0 and j=n.
* This will consolidate all the merged sorted lists to lists[0]
* Return list[0]

Time Complexity: O(m+n) * O(k)
Space Complexity: O(m+n)

Solved: [31/12/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""
from utils import ListNode, Utility

class Solution:
    def merge_k_sorted_lists(self, lists):
        if not lists:
            return None
        def merge2lists(list1, list2):
            if not list1:
                return list2
            if not list2:
                return list1
            temp = ListNode(-1)
            result = temp
            while list1 and list2:
                if list1.val<list2.val:
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
        size = len(lists)-1
        while size>=1:
            i, j = 0, size
            while i<j:
                lists[i] = merge2lists(lists[i], lists[j])
                i += 1
                j -= 1
            size = j
        return lists[0]

if __name__ == "__main__":
    sol = Solution()
    head1 = ListNode(1)
    head1.next = ListNode(4)
    head1.next.next = ListNode(5)

    head2 = ListNode(1)
    head2.next = ListNode(3)
    head2.next.next = ListNode(4)

    head3 = ListNode(2)
    head3.next = ListNode(6)

    util = Utility()

    lists = [head1, head2, head3]
    assert util.to_list(sol.merge_k_sorted_lists(lists)) == [1,1,2,3,4,4,5,6]
    assert util.to_list(sol.merge_k_sorted_lists([[]])) == []
    assert util.to_list(sol.merge_k_sorted_lists([])) == []
    print("✅ All tests passed!")