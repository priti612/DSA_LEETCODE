class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        ans=[]
        f=[0]*101
        for i in range(k):
            f[nums[i]+50]+=1
        def beauty():
            ct=0
            for val in range(-50,0):
                ct+=f[val+50]
                if ct>=x:
                    return val
            return 0
        ans.append(beauty())
        left=0
        for right in range(k,len(nums)):
            f[nums[left]+50]-=1
            left+=1
            f[nums[right]+50]+=1
            ans.append(beauty())
        return ans