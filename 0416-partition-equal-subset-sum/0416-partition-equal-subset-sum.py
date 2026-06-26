class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def subset(nums,sm):
            n=len(nums)
            t=[[False]*(sm+1) for _ in range(n+1)]
            for i in range(n+1):
                t[i][0]=True
            for i in range(1,n+1):
                for j in range(1,sm+1):
                    if nums[i-1]<=sm:
                        t[i][j]=t[i-1][j-nums[i-1]] or t[i-1][j]
                    else:
                        t[i][j]=t[i-1][j]
            return t[n][sm]
        
        n=len(nums)
        sm=sum(nums)
        if sm%2!=0:
            return False
        else:
            return subset(nums,sm//2)