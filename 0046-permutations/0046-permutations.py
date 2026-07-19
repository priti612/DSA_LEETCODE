class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def sol(idx,subset):
            if idx==len(nums):
                res.append(nums[:])
                return
            for i in range(idx,len(nums)):
                nums[idx],nums[i]=nums[i],nums[idx]
                sol(idx+1,nums)
                nums[idx],nums[i]=nums[i],nums[idx]
        sol(0,nums)
        return res