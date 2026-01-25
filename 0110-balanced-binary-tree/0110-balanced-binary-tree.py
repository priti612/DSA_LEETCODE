# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def check(root):
            if not root:
                return 0

            l=check(root.left)
            if l==-1:
                return -1
            r=check(root.right)
            if r==-1:
                return -1
            if abs(r-l)>1:
                return -1
            return max(l,r)+1
        return check(root)!=-1    