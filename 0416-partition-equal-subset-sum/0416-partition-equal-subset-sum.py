class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def subset(nums,targ):
            n=len(nums)
            t=[[False]*(targ+1) for _ in range(n+1)]
            for i in range(n+1):
                t[i][0]=True
            for i in range(1,n+1):
                for j in range(1,targ+1):
                    if nums[i-1]<=j:
                        t[i][j]=t[i-1][j-nums[i-1]] or t[i-1][j]
                    else:
                        t[i][j]=t[i-1][j]
            return t[n-1][targ]
        n=len(nums)
        summ=sum(nums)
        if summ%2!=0:
            return False
        elif summ%2==0:
            return subset(nums,summ//2)
        

        