# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.valid=True
        def dfs(root):
            if not root:
                return float('inf'),float('-inf')
            lmin,lmax=dfs(root.left)
            rmin,rmax=dfs(root.right)
            if lmax<root.val<rmin:
                return min(lmin,root.val),max(rmax,root.val)
            self.valid=False
            return float('-inf'),float('inf')
        dfs(root)
        return self.valid