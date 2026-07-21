# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        rightSide = []
        levels = {}
        q = deque()
        q.append((root, 1))
        while q:
            curr = q.popleft()
            if not levels.get(curr[1], False):
                levels[curr[1]] = True
                rightSide.append(curr[0].val)

            if curr[0].right:
                q.append((curr[0].right, curr[1] + 1))
            if curr[0].left:
                q.append((curr[0].left, curr[1] + 1))
            
        return rightSide