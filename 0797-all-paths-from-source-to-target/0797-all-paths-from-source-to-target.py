class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        t=len(graph)-1
        res=[]
        def dfs(i,p):
            if i==t:
                res.append(list(p))
                return
            for gp in graph[i]:
                p.append(gp)
                dfs(gp,p)
                p.pop()
        dfs(0,[0])
        return res