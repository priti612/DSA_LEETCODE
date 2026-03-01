# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=deque([root])
        ltor=True
        s=[]
        while q:
            n=len(q)
            st=[0]*n
            for i in range(n):
                # temp=TreeNode()
                temp=q.popleft()
                idx=i if ltor else n-i-1
                st[idx]=temp.val
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            ltor=not ltor
            s.append(st)
        return s

