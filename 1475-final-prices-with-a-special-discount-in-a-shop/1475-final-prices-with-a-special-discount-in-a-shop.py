class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans=[]
        for i in range(len(prices)):
            while ans and prices[ans[-1]]>=prices[i]:
                dis=ans.pop()
                prices[dis]-=prices[i]
            ans.append(i)
        return prices


