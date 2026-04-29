class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        mod=10**9+7
        gp=defaultdict(list)
        for i in range(len(prevRoom)):
            gp[prevRoom[i]].append(i)
        def dfs(node):
            if not gp[node]:
                return 1,1
            ans,l=1,0
            for p in gp[node]:
                t,r=dfs(p)
                ans=ans*t*(comb(l+r,r))%mod
                l+=r
            return ans,l+1
        sol=dfs(0)
        return sol[0]