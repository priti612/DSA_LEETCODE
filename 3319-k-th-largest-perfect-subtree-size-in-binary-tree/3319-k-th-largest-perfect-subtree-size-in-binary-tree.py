# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        
        res=[]
        def dfs(root):
            if not root:
                return 0
            l=dfs(root.left)
            r=dfs(root.right)
            if  l!=r:
                return -1
            sz=l+r+1
            res.append(sz)
            return sz
        dfs(root)
        if len(res)<k:
            return -1
        res.sort()
        return res[-k]



            