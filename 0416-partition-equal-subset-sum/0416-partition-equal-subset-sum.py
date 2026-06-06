class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm=sum(nums)
        if sm%2!=0:
            return False
        n=len(nums)
        trag=sm//2
        t=[[False]*(trag+1) for _ in range(n+1)]
        for i in range(n+1):
            t[i][0]=True
        for i in range(1,n+1):
            for j in range(1,trag+1):
                if nums[i-1]<=j:
                    t[i][j]=t[i-1][j] or t[i-1][j-nums[i-1]]
                else:
                    t[i][j]=t[i-1][j]
        return t[n][trag]

        