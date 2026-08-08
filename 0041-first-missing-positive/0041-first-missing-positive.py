class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # s=set(nums)
        # for i in range(1,len(nums)+1):
        #     if i not in s:
        #         return i
        # return len(nums)+1
        n=len(nums)
        for i in range(0,n):
            while 1<=nums[i]<=n and nums[nums[i]-1]!=nums[i]:
                ans=nums[i]-1
                nums[i],nums[ans]=nums[ans],nums[i]
        for i in range(1,n+1):
            if nums[i-1]!=i:
                return i
        return n+1