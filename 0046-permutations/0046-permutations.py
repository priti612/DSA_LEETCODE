class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def sol(i):
            if i==len(nums):
                res.append(nums[:])
                return
            
            for j in range(i,len(nums)):
                nums[i],nums[j]=nums[j],nums[i]
                sol(i+1)
                nums[i],nums[j]=nums[j],nums[i]
        sol(0)
        return res