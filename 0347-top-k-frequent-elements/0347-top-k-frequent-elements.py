class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ct=defaultdict(int)
        for i in nums:
            ct[i]+=1

        h=[]
        ans=[]
        for f,val in ct.items():
            heapq.heappush(h,(-val,f))

        for _ in range(k):

            val,f=heapq.heappop(h)
            ans.append(f)
            
        return ans