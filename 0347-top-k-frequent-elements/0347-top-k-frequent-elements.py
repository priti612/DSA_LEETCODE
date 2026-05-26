class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp={}
        for i in nums:
            mp[i]=mp.get(i,0)+1
        heap=[]
        for freq,val in mp.items():
            heapq.heappush(heap,(val,freq))
            if len(heap)>k:
                heapq.heappop(heap)
        ans=[]
        while k:
            freq,val=heapq.heappop(heap)
            ans.append(val)
            k-=1
        return ans
        
        