class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n=len(score)
        ans=[""]*n
        heap=[]

        for ind,val in enumerate(score):
            heapq.heappush(heap,(-val,ind))
        r=1
        while heap:
            val,idx=heapq.heappop(heap)
            if r==1:
                ans[idx]="Gold Medal"
            elif r==2:
                ans[idx]="Silver Medal"
            elif r==3:
                ans[idx]="Bronze Medal"
            else:
                ans[idx]=str(r)
            r+=1
        return ans
        
        