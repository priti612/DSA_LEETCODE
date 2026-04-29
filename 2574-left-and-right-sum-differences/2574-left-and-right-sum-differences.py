class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pre=[0]*n
        suff=[0]*n
        for i in range(1,n):
            pre[i]=pre[i-1]+nums[i-1]
        suff[-1]=0
        for i in range(n-2,-1,-1):
            suff[i]=suff[i+1]+nums[i+1]
        print(suff)
        ans=[]
        for i in range(n):
            ans.append(abs(pre[i]-suff[i]))
        return ans