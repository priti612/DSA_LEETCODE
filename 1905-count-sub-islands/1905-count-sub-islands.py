class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n=len(grid1)
        m=len(grid1[0])
        vis=set()
        
        def dfs(r,c):
            if min(r,c)<0 or r==n or c==m or grid2[r][c]==0 or (r,c) in vis:
                return True
            res=grid1[r][c]
            vis.add((r,c))
            res&=dfs(r+1,c)
            res&=dfs(r-1,c)
            res&=dfs(r,c-1)
            res&=dfs(r,c+1)
            return res
        ct=0
        for i in range(n):
            for j in range(m):
                if grid2[i][j]==1 and (i,j) not in vis:
                    if dfs(i,j):
                        ct+= 1
        return ct

        