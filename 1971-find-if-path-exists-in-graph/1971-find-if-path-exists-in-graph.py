class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        gp=defaultdict(list)
        for u,v in edges:
            gp[u].append(v)
            gp[v].append(u)
        s=set()
        def dfs(node):
            s.add(node)
            if node==destination:
                return True
            for nei in gp[node]:
                if nei not in s:
                    if dfs(nei):
                        return True
            return False
        return dfs(source)
