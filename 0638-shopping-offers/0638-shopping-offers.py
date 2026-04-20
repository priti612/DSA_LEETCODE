class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        f={}
        def dfs(needs):
            curr=tuple(needs)
            if curr in f:
                return f[curr]
            res=sum(needs[i]*price[i] for i in range(len(needs)) )
            
            for off in special:
                ans=[]
                for i in range(len(needs)):
                    if off[i]>needs[i]:
                        break
                    ans.append(needs[i]-off[i])
                if len(ans)==len(needs):
                    res=min(res,off[-1]+dfs(ans))
            f[curr]=res
            return res
            

        return dfs(needs)   