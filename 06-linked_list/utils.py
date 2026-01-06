from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Utility:
    def to_list(self, head: Optional[ListNode]):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result
