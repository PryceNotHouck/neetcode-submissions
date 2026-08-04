# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"

        result = []
        q = deque()
        q.append(root)
        while q:
            curr = q.popleft()
            if not curr:
                result.append("N")
            else:
                result.append(str(curr.val))
                q.append(curr.left)
                q.append(curr.right)

        print(".".join(result))
        return ".".join(result)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "N":
            return None

        vals = data.split(".")
        root = TreeNode(val = int(vals[0]))
        
        q = deque()
        q.append(root)
        i = 1
        while q:
            curr = q.popleft()
            if vals[i] != 'N':
                curr.left = TreeNode(val = int(vals[i]))
                q.append(curr.left)
            i += 1

            if vals[i] != 'N':
                curr.right = TreeNode(val = int(vals[i]))
                q.append(curr.right)
            i += 1

        return root