class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        V=len(points)
        adj=[[] for _ in range(V)]
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                x1=points[i][0]
                y1=points[i][1]
                x2=points[j][0]
                y2=points[j][1]
                d=abs(x1-x2)+abs(y2-y1)
                adj[i].append((j,d))
                adj[j].append((i,d))
            
        
        q=[(0,0)]
        ct=0
        vis=[False]*V
        while q:
            w,node=heapq.heappop(q)
            if vis[node]:
                continue
            vis[node]=True
            ct+=w
            for nei,wt in adj[node]:
                if not vis[nei]:
                    heapq.heappush(q,(wt,nei))
        return ct
        
                
