class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # ct=0
        # sm=0
        # for i in range(len(nums)):
        #     if nums[i]<=target:
        #         ct+=1
        #         sm+=nums[i]
        #         if sm<=target:
        #             ct+=1
        #         else:
        #             sm-=nums[i]
        # return ct
        nums.sort()
        left=0
        right=len(nums)-1
        ans=0
        mod=10**9+7
        while left<=right:
            if  nums[left]+nums[right]<=target:
                ans=(ans+pow(2,right-left,mod))%mod
                left+=1
            else:
                right-=1
        return ans