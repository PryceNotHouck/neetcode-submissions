# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        prev_group = dummy
        while True:
            i = k
            curr = prev_group
            while curr and i > 0:
                i -= 1
                curr = curr.next
            if not curr:
                break
            group = curr.next
            pivot = curr

            prev = group
            curr = prev_group.next
            while curr != group:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = prev_group.next
            prev_group.next = pivot
            prev_group = temp

        return dummy.next