class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n=len(cost)
        if n==2:
            return sum(cost)
        summ=0
        cost.sort(reverse=True)
        for i in range(0,n,3):
            summ+=cost[i]
            if i+1<n:
                summ+=cost[i+1]
        return summ