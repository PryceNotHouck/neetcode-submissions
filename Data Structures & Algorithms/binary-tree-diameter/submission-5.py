# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = deque()
        stack.append(root)

        mp = {}
        mp[None] = (0, 0)
        
        while stack:
            curr = stack[-1]

            if curr.left and curr.left not in mp:
                stack.append(curr.left)
            elif curr.right and curr.right not in mp:
                stack.append(curr.right)
            else:
                curr = stack.pop()

                leftHeight = mp[curr.left][0]
                leftDiameter = mp[curr.left][1]

                rightHeight = mp[curr.right][0]
                rightDiameter = mp[curr.right][1]

                mp[curr] = (1 + max(leftHeight, rightHeight), max(leftHeight + rightHeight, leftDiameter, rightDiameter))

        return mp[root][1]