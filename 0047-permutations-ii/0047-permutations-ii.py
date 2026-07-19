class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def sol(idx,nums):
            if idx==len(nums):
                res.append(nums[:])
                return
            s=set()
            for i in range(idx,len(nums)):
                if nums[i] in s:
                    continue
                s.add(nums[i])
                nums[idx],nums[i]=nums[i],nums[idx]
                sol(idx+1,nums)
                nums[idx],nums[i]=nums[i],nums[idx]

        sol(0,nums)
        return res