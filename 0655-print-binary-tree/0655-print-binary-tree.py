class Solution:
    def printTree(self,root):
        def height(node):
            if not node:
                return -1
            return 1+max(height(node.left),height(node.right))
        h=height(root)
        m=h+1
        n=2**m-1
        res=[[""]*n for _ in range(m)]
        def dfs(node,r,c):
            if not node:
                return
            res[r][c]=str(node.val)
            if node.left:
                dfs(node.left,r+1,c-2**(h-r-1))
            if node.right:
                dfs(node.right,r+1,c+2**(h-r-1))
        dfs(root,0,(n-1)//2)
        return res     