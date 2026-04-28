class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        d={}
        def dfs(i,j,curr):
            if i<0 or i>=row or j<0 or j>=col or matrix[i][j]<=curr:
                return 0
            if (i,j) in d:
                return d[(i,j)]
            res=1
            res=max(res,1+dfs(i+1,j,matrix[i][j]))
            res=max(res,1+dfs(i-1,j,matrix[i][j]))
            res=max(res,1+dfs(i,j+1,matrix[i][j]))
            res=max(res,1+dfs(i,j-1,matrix[i][j]))

            d[(i,j)]=res
            return res

        row=len(matrix)
        col=len(matrix[0])
        ct=0
        for r in range(row):
            for c in range(col):
                dfs(r,c,-1)
        return max(d.values())
