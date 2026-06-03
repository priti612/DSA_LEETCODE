class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        
        n=len(cost)
        t=[0]*(n+1)
        t[0]=cost[0]
        t[1]=cost[1]
        ct=0
        if n==1:
            return cost[0]
        for i in range(2,n):
            t[i]=cost[i]+min(t[i-1],t[i-2])
        return min(t[n-1],t[n-2])