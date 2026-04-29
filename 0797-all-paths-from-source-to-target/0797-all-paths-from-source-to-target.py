class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        targ=len(graph)-1
        res=[]
        def dfs(i,path):
            if i==targ:
                res.append(list(path))
                return
            for gp in graph[i]:
                path.append(gp)
                dfs(gp,path)
                path.pop()


        dfs(0,[0])
        return res