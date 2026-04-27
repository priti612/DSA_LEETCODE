# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root,t):

            if not root:
                return 0
            ct=0
            if t==root.val:
                ct+=1
            ct+=dfs(root.left,t-root.val)
            ct+=dfs(root.right,t-root.val)
            return ct
        if not root:
            return 0
        return dfs(root,targetSum)+self.pathSum(root.left,targetSum)+self.pathSum(root.right,targetSum)
