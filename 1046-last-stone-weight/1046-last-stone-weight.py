class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        st=[]
        for i in range(len(stones)):
            heapq.heappush(st,-(stones[i]))
        while len(st)>=2:
            x=heapq.heappop(st)
            y=heapq.heappop(st)
            if x!=y:
                heapq.heappush(st,-abs(y-x))
        return -st[0] if st else 0

