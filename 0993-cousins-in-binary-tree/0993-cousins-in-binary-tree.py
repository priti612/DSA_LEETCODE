# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], a: int, b: int) -> bool:
        if not root:
            return False
        q=deque([root])
        while q:
            n=len(q)
            l1=l2=False
            for _ in range(n):
                temp=q.popleft()
                if temp.val==a:
                    l1=True
                if temp.val==b:
                    l2=True
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            if l1!=l2:
                return False
            if l1 and l2:
                found=True
                break
        if not found:
            return False
        return not self.parent(root,a,b)
    def parent(self,root,a,b):
        if not root:
            return False
        if root.left and root.right:
            if root.left.val==a and root.right.val==b:
                return True
            if root.right.val==a and root.left.val==b:
                return True
        return self.parent(root.right,a,b) or self.parent(root.left,a,b)