class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for idx,val in enumerate(stones):
            heapq.heappush(heap,(-val,idx))
        ans=[]
        while len(heap)>1:
            x,idx=heapq.heappop(heap)
            y,idx1=heapq.heappop(heap)
            if x!=y:
                heapq.heappush(heap,(x-y,idx))
        return -heap[0][0] if heap else 0



