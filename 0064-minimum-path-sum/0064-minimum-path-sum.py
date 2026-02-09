class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        r=len(grid)
        c=len(grid[0])
        
        for i in range(r):
            for j in range(c):
                if i==0 and j==0:
                    continue 
                elif i==0:
                    grid[0][j]+=grid[0][j-1]
                elif j==0:
                    grid[i][0]+=grid[i-1][0]
                else:
                    grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
        return grid[r-1][c-1]