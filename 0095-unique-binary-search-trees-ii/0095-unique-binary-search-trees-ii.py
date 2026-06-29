# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self,n:int)->List[Optional[TreeNode]]:
        def dfs(l,r):
            if l>r:
                return [None]
            res=[]
            for i in range(l,r+1):
                left=dfs(l,i-1)
                right=dfs(i+1,r)
                for a in left:
                    for b in right:
                        root=TreeNode(i)
                        root.left=a
                        root.right=b
                        res.append(root)
            return res
        return dfs(1,n)