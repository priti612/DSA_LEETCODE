class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi=nums[0]
        sm=nums[0]
        
        for i in range(1,len(nums)):
            if sm>=0:
                sm+=nums[i]
            else:
                sm=nums[i]
            
            if sm>maxi:
                maxi=sm
        return maxi