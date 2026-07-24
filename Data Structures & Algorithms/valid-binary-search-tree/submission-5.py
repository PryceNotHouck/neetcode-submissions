# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque()
        q.append((root, float("-inf"), float("inf")))
        while q:
            curr, leftBound, rightBound = q.popleft()

            if not (leftBound < curr.val < rightBound):
                return False

            if curr.left:
                q.append((curr.left, leftBound, curr.val))
            if curr.right:
                q.append((curr.right, curr.val, rightBound))

        return True