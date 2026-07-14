# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q=deque()
        ans=0
        q.append(root)
        sum=0
        maxSum=float("-inf")
        i=0
        while q:
            sum=0
            i+=1
            for _ in range(len(q)):
                curr=q.popleft()
                sum+=curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            if sum>maxSum:
                maxSum=sum
                ans=i
            
        return ans


