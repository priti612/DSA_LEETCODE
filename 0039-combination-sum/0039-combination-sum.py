class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        def sol(idx,tot,subset):
            if tot==target:
                res.append(subset.copy())
                return
            if tot>target:
                return
            
            for i in range(idx,len(nums)):
                subset.append(nums[i])
                sm=tot+nums[i]
                sol(i,sm,subset)
                sm=tot
                subset.pop()
                
            
        res=[]
        sol(0,0,[])
        return res