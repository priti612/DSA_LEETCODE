class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        vis=set()
        res=[]
        def dfs(node):
            vis.add(node)
            res.append(node)
            for nei in adj[node]:
                if nei not in vis:
                    dfs(nei)
        dfs(source)
        for i in range(len(res)):
            if res[i]==destination:
                return True
        return False





