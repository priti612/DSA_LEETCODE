# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        if not root:
            return ans
        q=deque([root])
        while q:
            n=len(q)
            for i in range(n):
                temp=q.popleft()
                if i==0:
                    ans.append(temp.val)
                if temp.right:
                    q.append(temp.right)
                if temp.left:
                    q.append(temp.left)
        return ans