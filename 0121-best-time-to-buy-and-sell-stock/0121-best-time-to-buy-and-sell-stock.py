class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # mini=min(prices)
        # idx=prices.index(mini)
        # maxi=max(prices[idx:])
        # return maxi-mini
        maxi=0
        mini=prices[0]
        for i in range(1,len(prices)):
            if prices[i]<mini:
                mini=prices[i]
            else:
                curr=prices[i]-mini
                   
                maxi=max(maxi,curr)
                
        return maxi