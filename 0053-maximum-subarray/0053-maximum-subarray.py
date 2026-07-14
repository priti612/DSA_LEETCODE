class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=nums[0]
        sm=0
        for i in range(len(nums)):
            sm+=nums[i]
            maxi=max(sm,maxi)
            if sm<0:
                sm=0
        return maxi