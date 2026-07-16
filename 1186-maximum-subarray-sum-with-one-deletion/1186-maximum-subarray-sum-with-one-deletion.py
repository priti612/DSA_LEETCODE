class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        one=nums[0]
        no=nums[0]
        mx=nums[0]
        for i in range(1,len(nums)):
            tmp=max(no,one+nums[i])
            no=max(nums[i],no+nums[i])
            one=tmp
            mx=max(one,no,mx)
        return mx
            
