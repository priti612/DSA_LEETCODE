class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def tgsm(nums,target):
            n=len(nums)
            t=[[0]*(target+1) for _ in range(n+1)]
            t[0][0]=1
            for i in range(1,n+1):
                for j in range(target+1):
                    if nums[i-1]<=j:
                        t[i][j]=t[i-1][j] + t[i-1][j-nums[i-1]]
                    else:
                        t[i][j]=t[i-1][j]
            return t[n][target]
        sm=sum(nums)
        tg=(sm+target)//2
        if (sm+target)%2!=0 or abs(tg)>sm:
            return 0
        if tg<0:
            return 0
        return tgsm(nums,tg)