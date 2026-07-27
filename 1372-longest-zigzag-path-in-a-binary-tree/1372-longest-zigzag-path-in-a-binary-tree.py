class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ans=0

        def f(node,left,right):
            nonlocal ans
            if not node:
                return
            
            ans=max(ans,left,right)
            f(node.left,right+1,0)
            f(node.right,0,left+1)
        
        f(root,0,0)
        return ans
       