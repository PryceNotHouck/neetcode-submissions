# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root: Optional[TreeNode]) -> list:
        if not root:
            return []

        arr = []
        stack = deque()
        stack.append(root)
        arr.append(root.val)
        while stack:
            curr = stack.pop()

            if curr.left:
                stack.append(curr.left)
                arr.append(curr.left.val)
            else:
                arr.append(None)
            
            if curr.right:
                stack.append(curr.right)
                arr.append(curr.right.val)
            else:
                arr.append(None)
        return arr

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p) == self.dfs(q)