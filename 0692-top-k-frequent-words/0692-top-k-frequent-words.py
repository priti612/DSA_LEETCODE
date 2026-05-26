class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mp={}
        for i in words:
            mp[i]=mp.get(i,0)+1
        heap=[]
        for f,v in mp.items():
            heapq.heappush(heap,(-v,f))
            
        ans=[]
        while k:
            x,y =heapq.heappop(heap)
            ans.append(y)
            k-=1
        return ans