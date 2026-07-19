class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        nums.sort()
        def sol(idx,subset):
            if idx==len(nums):
                res.append(tuple(subset))
                return
            
            subset.append(nums[idx])
            sol(idx+1,subset)
            subset.pop()
            while idx+1<len(nums) and nums[idx]==nums[idx+1]:
                idx+=1
            sol(idx+1,subset)
            
        sol(0,[])
        return [list(i) for i in res]