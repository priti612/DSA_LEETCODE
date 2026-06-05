class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        maxi=float('inf')
        t=[0]*(amount+1)
        
        for i in range(1,amount+1):
            t[i]=maxi
            for c in coins:
                if c<=i and t[i-c]!=maxi:
                    t[i]=min(1+t[i-c],t[i])
                
        res=t[amount]
        return res if res!=maxi else -1
                                                                                         