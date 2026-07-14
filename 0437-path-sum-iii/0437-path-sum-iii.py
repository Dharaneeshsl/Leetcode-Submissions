class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        pre={0:1}
        ans=0
        def dfs(node,currsum):
            nonlocal ans
            if not node:
                return

            currsum+=node.val
            ans+=pre.get(currsum-targetSum,0)
            pre[currsum]=pre.get(currsum,0)+1
            dfs(node.left,currsum)
            dfs(node.right,currsum)
            pre[currsum]-=1
        dfs(root,0)
        return ans