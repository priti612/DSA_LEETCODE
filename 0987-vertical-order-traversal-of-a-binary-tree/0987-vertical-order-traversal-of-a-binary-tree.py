# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dt=defaultdict(list)
        dq=deque([(root,0,0)])
        if not root:
            return []
        while dq:
            node,row,col=dq.popleft()
            dt[col].append([row,node.val])
            if node.left:
                dq.append((node.left,row+1,col-1))
            if node.right:
                dq.append((node.right,row+1,col+1))
        ans=[]
        for cols in sorted(dt):
            dt[cols].sort()
            tmp=[]
            for row, val in dt[cols]:
                tmp.append(val)
            ans.append(tmp)
        return ans
