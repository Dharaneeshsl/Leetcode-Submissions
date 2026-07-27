# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent={}
        def dfs(node,par):
            if not node:
                return
            parent[node]=par
            dfs(node.left,node)
            dfs(node.right,node)
        dfs(root,None)
        q=deque([(target,0)])
        vis={target}
        ans=[]
        while q:
            node,d=q.popleft()
            if d==k:
                ans.append(node.val)
            elif d<k:
                for nei in (node.left,node.right,parent[node]):
                    if nei and nei not in vis:
                        vis.add(nei)
                        q.append((nei,d+1))
        return ans