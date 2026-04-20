class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=prices[0]
        sub=0
        for i in range(1,len(prices)):
            if prices[i]<maxi:
                maxi=prices[i]
            else:
                sub=max(sub,prices[i]-maxi)
        return sub