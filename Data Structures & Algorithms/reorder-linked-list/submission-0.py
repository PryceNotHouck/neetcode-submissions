# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = deque()
        
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next

        curr = stack.popleft()
        while stack:
            curr.next = stack.pop()
            curr = curr.next
            if stack:
                curr.next = stack.popleft()
                curr = curr.next
        
        curr.next = None