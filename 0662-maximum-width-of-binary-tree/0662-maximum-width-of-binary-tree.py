# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return []
        q=deque()
        q.append((root,0))
        res=0
        while q:
            n=len(q)
            r,st=q[0]
            for i in range(n):
                node,ind=q.popleft()
                ind-=st
                if i==n-1:
                    res=max(res,ind+1)
                if node.left:
                    q.append((node.left,2*ind))
                if node.right:
                    q.append((node.right,2*ind+1))
        return res