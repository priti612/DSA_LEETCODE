class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=defaultdict(list)
        for u,v,w in times:
            adj[u].append((v,w))
        print(adj)
        
        dist=[float('inf')]*(n+1)
        dist[k]=0
        heap=[(0,k)]
        while heap:
            time,u=heapq.heappop(heap)
            if time > dist[u]:
                continue
            for v,wt in adj[u]:
                if dist[u]+wt<dist[v]:
                    dist[v]=dist[u]+wt
                    heapq.heappush(heap,(dist[v],v))
            maxi=max(dist[1:])
        return maxi if maxi!=float('inf')  else -1


