# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi=float('-inf')
        def dfs(root):
            if not root:
                return 0
            lmin=max(dfs(root.left),0)
            rmin=max(dfs(root.right),0)
            curr=root.val+lmin+rmin
            self.maxi=max(curr,self.maxi)
                
            return root.val+max(lmin,rmin)
        dfs(root)
        return self.maxi