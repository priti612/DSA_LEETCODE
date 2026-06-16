class Solution:
    class DSU:
        def __init__(self, V: int):
            self.pat=[0]*(V)
            for i in range(V):
                self.pat[i]=i
            self.rank=[0]*V

        def find(self,i):
            if self.pat[i]==i:
                return i
            self.pat[i]=self.find(self.pat[i])
            return self.pat[i]
        def union(self,u,v):
            pu=self.find(u)
            pv=self.find(v)
            if pu==pv:
                return False
            if self.rank[pu]<self.rank[pv]:
                self.pat[pu]=pv
            elif self.rank[pv]<self.rank[pu]:
                self.pat[pv]=pu
            else:
                self.pat[pv]=pu
                self.rank[pu]+=1
            return True
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        dsu=self.DSU(n)
        ct=n
        if len(connections)<ct-1:
            return -1
        for u,v in connections:
            if dsu.union(u,v):
                ct-=1
        return ct-1



        

        
        