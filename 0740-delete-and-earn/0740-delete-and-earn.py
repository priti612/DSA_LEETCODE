class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        mx=max(nums)
        dp=[0]*(mx+1)
        p=[0]*(mx+1)
        if len(nums)==1:
            return nums[0]
        
        for num in nums:
            p[num]+=num
        # dp[0]=nums[0]
        # dp[1]=max(nums[0],nums[1])
        dp[1]=p[1]
        for i in range(2,mx+1):
            dp[i]=max(dp[i-1],dp[i-2]+p[i])
        return dp[mx]