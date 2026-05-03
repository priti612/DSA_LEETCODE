class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        inc=[0]*(n+1)
        gp=defaultdict(list)
        for st,end,p in flights:
            gp[st].append((end,p))
        h=[(0,src,0)] 
        dp={} 
        while h:
            ct,node,st=heapq.heappop(h)
            if node==dst:
                return ct
            if st>k:
                continue 
            
            if node in dp and dp[node]<=st:
                continue 
            dp[node]=st
            for nei , p in gp[node]:
                heappush(h,(ct+p,nei,st+1))
        return -1


