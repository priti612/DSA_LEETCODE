class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        f={}
        def sol(i,free):
            n=len(prices)
            uq=(i,free)
            if i==n:
                return 0
            if (i,free) in f:
                return f[uq]
            cost1=prices[i]+sol(i+1,2*i+2) # cost ko cal
            if i<free:
                cost2=sol(i+1,free)
            else:
                cost2=float('inf')
            f[uq]=min(cost1,cost2)
            return f[uq]
            
            

        return sol(0,0)