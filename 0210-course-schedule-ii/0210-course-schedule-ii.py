class Solution:
    def findOrder(self, num: int, pre: List[List[int]]) -> List[int]:
        gp=defaultdict(list)
        indg=[0]*num
        for u,v in pre:
            indg[u]+=1
            gp[v].append(u)
        vis=set()
        st=[]
        def dfs(node):
            st.append(node)
            indg[node]=-1
            for nei in gp[node]:
                indg[nei]-=1
                if indg[nei]==0:
                    dfs(nei)
        for i in range(num):
            if indg[i]==0:
                dfs(i)
        return st if len(st)==num else []
            
                