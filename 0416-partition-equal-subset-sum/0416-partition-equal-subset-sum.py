class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def subset(arr,targ):
            n=len(arr)
            t=[[False]*(targ+1) for _ in range(n+1)]
            for i in range(n+1):
                t[i][0]=True
            for i in range(1,n+1):
                for j in range(1,targ+1):
                    if arr[i-1]<=j:
                        t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]
                    else:
                        t[i][j]=t[i-1][j]
            return t[n-1][targ]
        n=len(nums)
        sm=sum(nums)
        if sm%2!=0:
            return False
        elif sm%2==0:
            return subset(nums,sm//2)

