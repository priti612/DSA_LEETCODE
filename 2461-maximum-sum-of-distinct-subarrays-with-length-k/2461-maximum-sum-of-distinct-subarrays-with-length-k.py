class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxi=0
        
        ct=Counter()
        sm=0
        for i in range(len(nums)):
            ct[nums[i]]+=1
            sm+=nums[i]
            if i>=k:
                l=nums[i-k]
                ct[l]-=1
                
                sm-=l
                if ct[l]==0:
                    del ct[l]
            if len(ct)==k and i>=k-1:
                maxi=max(maxi,sm)
        return maxi