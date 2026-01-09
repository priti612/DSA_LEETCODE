# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def height(root):
            if not root:
                return 0
            return max(height(root.left),height(root.right))+1
        l=height(root.left)
        r=height(root.right)
        if l==r:
            return root
        if l>r:
            return self.lcaDeepestLeaves(root.left)
        else:
            return self.lcaDeepestLeaves(root.right)
        