class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        ans=[]
        h=[-x for x in piles]
        heapq.heapify(h)
        
        while k>0:
            curr=heapq.heappop(h)
            new_val=floor(curr/2)
            heappush(h,new_val)
            k-=1
            
        return -sum(h)