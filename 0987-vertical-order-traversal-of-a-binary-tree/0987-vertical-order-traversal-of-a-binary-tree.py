# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        def bt(root,row,col):
            if not root:
                return
            res.append([col,row,root.val])
            bt(root.left,row+1,col-1)
            bt(root.right,row+1,col+1)
        bt(root,0,0)
        res.sort()
        prev=float('-inf')
        op=[]
        for col,row,node in res:
            if col!=prev:
                op.append([])
                prev=col
            op[-1].append(node)
        return op

