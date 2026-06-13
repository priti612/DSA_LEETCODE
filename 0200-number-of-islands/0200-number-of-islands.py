class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def sol(i,j):
            if i>=len(grid) or j>=len(grid[0]) or i<0 or j<0  or grid[i][j]=="0":
                return
            grid[i][j]="0"
            sol(i+1,j)
            sol(i,j+1)
            sol(i,j-1)
            sol(i-1,j)



        ct=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=="1":
                    ct+=1
                    sol(r,c)
                    
        return ct