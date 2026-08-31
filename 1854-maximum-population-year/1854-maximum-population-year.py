class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        pp=[0]*101
        for b,d in logs:
            for y in range(b,d):
                pp[y-1950]+=1
        mx=max(pp)
        return 1950+pp.index(mx)