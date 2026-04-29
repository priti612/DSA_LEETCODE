class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        one=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    one+=1
        print(q)
        d=[(1,0),(-1,0),(0,1),(1,0)]
        ct=0
        while q and one>0:
            ct+=1
            for _ in range(len(q)):
                x,y=q.popleft()
            
                for dr,dc in d:
                    nr,nc=x+dr,y+dc
                    if nr<0 or nr>=len(grid) or nc<0 or nc>=len(grid[0]) or grid[nr][nc]==2 or grid[nr][nc]==0:
                        continue 
                    else:
                        one-=1
                        grid[nr][nc]=2
                        q.append((nr,nc))
            
        print(q)
        return ct if one==0 else -1
