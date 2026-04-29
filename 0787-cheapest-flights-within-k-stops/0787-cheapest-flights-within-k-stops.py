class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        gp=defaultdict(list)
        for f,t,cost in flights:
            gp[f].append((t,cost))
        print(gp)
        heap=[(0,src,0)]
        vis={}
        while heap:
            ct,node,st=heapq.heappop(heap)
            if node==dst:
                return ct
            if st>k:
                continue
            if node in vis and vis[node]<=st:
                continue
            
            vis[node]=st
             
            for nei,p in gp[node]:
                heappush(heap,(ct+p,nei,st+1))
        return -1

