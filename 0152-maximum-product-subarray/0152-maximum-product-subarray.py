class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi=nums[0]
        mini=nums[0]
        mx=nums[0]
        for i in range(1,len(nums)):
            v=nums[i]
            if v<0:
                maxi,mini=mini,maxi
            maxi=max(v,v*maxi)
            mini=min(v,v*mini)
            mx=max(maxi,mx)
        return mx
                
