# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def height(root):
            if not root:
                return 0
            l=height(root.left)
            r=height(root.right)
            return max(l,r)+1
        l=height(root.left)
        r=height(root.right)
        if r==l:
            return root
        
        if r>l:
            return self.subtreeWithAllDeepest(root.right)
        else:
            return self.subtreeWithAllDeepest(root.left)
        