class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def sol(idx,subset):
            if idx==len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[idx])
            sol(idx+1,subset)
            subset.pop()
            sol(idx+1,subset)
        sol(0,[])
        return res