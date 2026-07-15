# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        head = ListNode()
        curr = head
        while any(lists):
            curr_val = 1000
            for node in lists:
                if node:
                    curr_val = min(curr_val, node.val)

            for i, node in enumerate(lists):
                while node and node.val == curr_val:
                    curr.next = node
                    curr = curr.next
                    node = node.next
                    lists[i] = node
                
        return head.next