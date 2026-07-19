class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def sol(idx,comb):
            if k==len(comb):
                res.append(comb.copy())
                return
            for i in range(idx,n+1):
                comb.append(i)
                sol(i+1,comb)
                comb.pop()
                

        sol(1,[])
        return res