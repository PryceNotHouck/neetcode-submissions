# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bfsString(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        bfs = ""
        stack = [root]
        while stack:
            curr = stack.pop()
            bfs += str(curr.val)
            
            if curr.left:
                stack.append(curr.left)
                bfs += str(curr.left.val)
            else:
                bfs += "0"

            if curr.right:
                stack.append(curr.right)
                bfs += str(curr.right.val)
            else:
                bfs += "0"
        return bfs

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.bfsString(subRoot) in self.bfsString(root)