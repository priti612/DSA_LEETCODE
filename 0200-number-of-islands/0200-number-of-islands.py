class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(a,b):
            if a<0 or a>=len(grid) or b<0 or b>=len(grid[0]) or grid[a][b]=='0':
                return
            grid[a][b]='0'
            dfs(a+1,b)
            dfs(a-1,b)
            dfs(a,b+1)
            dfs(a,b-1)
        ct=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    ct+=1
                    dfs(i,j)
           
        return ct