# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        def sol(root,par,grap):

            if not root:
                return 0
            sm=0
            if grap and grap.val %2==0:
                sm+=root.val
            sm+=sol(root.left,root,par)
            sm+=sol(root.right,root,par)
            return sm
        return sol(root,None,None)