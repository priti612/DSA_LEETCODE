# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.maxi=0
        def dfs(root):
            if not root:
                return float('inf'),float('-inf'),0  # min,max,sm
            lmin,lmax,lsm=dfs(root.left)
            rmin,rmax,rsm=dfs(root.right)
            if lmax<root.val<rmin:
                curr=root.val+lsm+rsm
                self.maxi=max(self.maxi,curr)
                return min(lmin,root.val),max(rmax,root.val),curr
            return float('-inf'),float('inf'),0
        dfs(root)
        return self.maxi
        