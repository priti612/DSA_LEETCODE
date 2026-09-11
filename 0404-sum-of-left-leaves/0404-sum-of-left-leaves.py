# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        def leftsum(root):
            if not root:
                return 0
            tot=0
            if root.left and not root.left.left and not root.left.right:
                tot+=root.left.val
            else:
            
                tot+=leftsum(root.left)
            tot+=leftsum(root.right)
            return tot
        return leftsum(root)
        