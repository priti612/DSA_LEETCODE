class Solution:
    def combinationSum2(self, candidates: List[int], tot: int) -> List[List[int]]:
        candidates.sort()
        def sol(idx,tot,subset):
            if tot==0:
                res.append(subset.copy())
                return
            if tot<0:
                return
            for i in range(idx,len(candidates)):
                if i>idx and candidates[i]==candidates[i-1]:
                    continue
                subset.append(candidates[i])
                sm=tot-candidates[i]
                sol(i+1,sm,subset)
                subset.pop()
        res=[]
        sol(0,tot,[])
        return res