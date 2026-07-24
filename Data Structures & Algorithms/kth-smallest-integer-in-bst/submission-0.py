# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        vals = set()
        q = deque()
        q.append(root)
        
        while q:
            curr = q.popleft()
            vals.add(curr.val)

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        index = 0
        for v in vals:
            index += 1
            if index == k:
                return v

        return 0