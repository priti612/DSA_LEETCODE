class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxi=0
        sm=0
        f={0:-1}
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]=-1
            sm+=nums[i]
            if sm in f:
                idx=i-f[sm]
                maxi=max(maxi,idx)
            else:
                f[sm]=i  # first time dekhe hai
        return maxi