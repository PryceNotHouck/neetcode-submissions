# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        i = 0
        while curr:
            i += 1
            curr = curr.next

        remove = i - n
        i = 0

        if not remove:
            return head.next

        curr = head
        prev = None
        while curr:
            if i == remove:
                if prev:
                    prev.next = curr.next
                curr = None
                break
            else:
                prev = curr
                curr = curr.next
                i += 1

        return head