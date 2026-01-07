# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        MOD=10**9+7
        self.maxi=0
        
        
        # curr_sum=0
        def tot_sum(root):
            if not root:
                return 0
            left=tot_sum(root.left)
            right=tot_sum(root.right)
            return left+right+root.val
        summ=tot_sum(root)
        def dfs(root):
            if not root:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            curr_sum=left+right+root.val
            self.maxi=max(self.maxi,(summ-curr_sum)*curr_sum)
            return curr_sum
        dfs(root)
        return self.maxi%MOD