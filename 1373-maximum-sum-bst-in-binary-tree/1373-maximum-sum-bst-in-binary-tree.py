# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans=0
        def dfs(node):
            nonlocal ans
            if not node:
                return True,float('inf'),float('-inf'),0
            lbst,lmin,lmax,lsum=dfs(node.left)
            rbst,rmin,rmax,rsum=dfs(node.right)
            if lbst and rbst and lmax<node.val<rmin:
                s=lsum+rsum+node.val
                ans=max(ans,s)
                return True,min(lmin,node.val),max(rmax,node.val),s
            return False,0,0,0
        dfs(root)
        return ans