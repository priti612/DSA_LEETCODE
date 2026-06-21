class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        maxi=amount+1
        n=len(coins)
        t=[[maxi]*(amount+1) for _ in range(n+1)]

        for i in range(n+1):
            t[i][0]=0
        for i in range(1,n+1):
            for j in range(1,amount+1):
                if coins[i-1]<=j:
                    t[i][j]=min(t[i-1][j],1+t[i][j-coins[i-1]])
                else:
                    t[i][j]=t[i-1][j]
        ans=t[n][amount]
        return ans if ans<=amount else -1
                                                                                         