class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        t=[1]*n
        for i in range(1,n):
            for j in range(0,i):
                if nums[j]<nums[i]:
                    t[i]=max(t[i],1+t[j])
        return max(t)