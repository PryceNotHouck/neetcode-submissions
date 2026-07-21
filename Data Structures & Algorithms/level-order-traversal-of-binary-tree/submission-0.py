# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append((root, 1))
        groups = [[]]
        prev = None
        while q:
            curr = q.popleft()
            if prev and curr[1] > prev[1]:
                groups.append([])
            groups[-1].append(curr[0].val)

            if curr[0].left:
                q.append((curr[0].left, curr[1] + 1))
            if curr[0].right:
                q.append((curr[0].right, curr[1] + 1))
            prev = curr

        return groups