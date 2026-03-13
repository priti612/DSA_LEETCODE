class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=nums[0]
        subarr=nums[0]
        for i in range(1,len(nums)):
            curr=max(curr+nums[i],nums[i])
            subarr=max(curr,subarr)
        return subarr