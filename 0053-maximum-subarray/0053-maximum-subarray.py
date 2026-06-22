class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sm=0
        maxi=float('-inf')
        for i in range(len(nums)):
            sm+=nums[i]
            maxi=max(maxi,sm)
            if sm<0:
                sm=0
        return maxi