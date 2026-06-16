class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def dfs(ver,vis,adj):
            vis[ver]=True
            ctp=[ver]
            for nei in adj[ver]:
                if not vis[nei]:
                    ctp.extend(dfs(nei,vis,adj))
            return ctp
        
        ct=0
        vis=[False]*n
        for i in range(n):
            if not vis[i]:
                comp=dfs(i,vis,adj)
                is_comp=True
                cpt=len(comp)-1
                for node in comp:
                    if len(adj[node])!=cpt:
                        is_comp=False
                        break
                if is_comp:
                    ct+=1
        return ct