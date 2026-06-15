class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        adj=[[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1 and i!=j:
                    adj[i].append(j)
        

        def dfs(i):
            vis[i]=True
            for nei in adj[i]:
                if not vis[nei]:
                    
                    dfs(nei)


        
        vis=[False]*n
        ct=0
        for i in range(n):
            if not vis[i]:
                dfs(i)
                ct+=1
        return ct