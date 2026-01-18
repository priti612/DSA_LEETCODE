class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def knp(nums,targ):
            n=len(nums)
            t=[[0]*(targ+1) for _ in range(n+1)]
            t[0][0]=1
            for i in range(1,n+1):
                for j in range(targ+1):
                    if nums[i-1]<=j:
                        t[i][j]=t[i-1][j-nums[i-1]]+t[i-1][j]
                    else:
                        t[i][j]=t[i-1][j]
            return t[n][targ]
        n=len(nums)
        s1=sum(nums)
        targ=(target+s1)//2
        if (target+s1)%2!=0 or abs(target)>s1:
            return 0
        return knp(nums,targ)



