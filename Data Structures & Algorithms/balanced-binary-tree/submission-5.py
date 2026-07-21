# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = []
        stack.append(root)
        depths = {root : 1}
        
        last = None
        curr = root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack[-1]
                if not curr.right or last == curr.right:
                    stack.pop()
                    left = depths.get(curr.left, 0)
                    right = depths.get(curr.right, 0)

                    if abs(left - right) > 1:
                        return False
                    else:
                        depths[curr] = max(left, right) + 1
                        last = curr
                        curr = None
                else:
                    curr = curr.right

        return True