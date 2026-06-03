class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*(n+1)
        dp[0]=nums[0]
        if n==0:
            return 0
        if n==1:
            return nums[0]
        dp[0]=nums[0]
        dp[1]=max(nums[1],nums[0])
        for i in range(2,n):
            tk=nums[i]+dp[i-2]
            nottk=dp[i-1]
            maxi=max(tk,nottk)
            dp[i]=maxi
        return dp[n-1]