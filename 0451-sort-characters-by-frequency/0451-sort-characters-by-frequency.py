class Solution:
    def frequencySort(self, s: str) -> str:
        heap=[]
        ct=Counter(s)
        for idx,val in ct.items():
            
            heapq.heappush(heap,(-val,idx))
        res=[]
        while heap:
            idx,val=heapq.heappop(heap)
            res.append(val*-idx)
        return "".join(res)