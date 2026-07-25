class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        if grid[0][0]==1 or grid[-1][-1]==1:
            return -1
        d = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
        q=deque([(0,0,1)])

        vis=set()
        vis.add((0,0))
        while q:
            x=len(q)
            for _ in range(x):
                r,c,ct=q.popleft()
                if r==n-1 and c==m-1:
                    return ct
                for dr,dc in d:
                    nr=r+dr
                    nc=c+dc
                    if 0<=nr<n and 0<=nc<m and grid[nr][nc]==0 and (nr,nc) not in vis:
                        # grid[nr][nc]=1
                        vis.add((nr,nc))
                        q.append((nr,nc,ct+1))
        return -1
        
        
                

                
                