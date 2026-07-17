# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque()
        q.append((root, 1))
        maxD = 0
        while q:
            curr = q.popleft()
            maxD = max(maxD, curr[1])

            if curr[0].left:
                q.append((curr[0].left, curr[1] + 1))
            if curr[0].right:
                q.append((curr[0].right, curr[1] + 1))

        return maxD