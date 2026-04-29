class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        gp=defaultdict(list)
        for u,v,w in times:
            gp[u].append((v,w))
        print(gp)
    
        minheap=[(0,k)]
        vis={}
        while minheap:
            t,curr=heappop(minheap)
            if curr in vis:
                continue
            vis[curr]=t
            for nei,w in gp[curr]:
                heappush(minheap,(t+w,nei))
        if len(vis)!=n:
            return -1
        return max(vis.values()) 
