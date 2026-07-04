class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m,n=len(mat),len(mat[0])
        l,r=0,n-1

        while l<=r:
            mid=(l+r)//2
            max_row=0
            for i in range(m):
                if mat[i][mid]>mat[max_row][mid]:
                    max_row=i

            left=mat[max_row][mid-1] if mid-1>=0 else -1
            right=mat[max_row][mid+1] if mid+1<n else -1
            curr=mat[max_row][mid]

            if curr>left and curr>right:
                return [max_row,mid]
            if right>curr:
                l = mid+1
            else:
                r = mid-1