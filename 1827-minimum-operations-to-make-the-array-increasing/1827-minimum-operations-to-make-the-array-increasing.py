class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        ct=0
        for i in range(len(nums)-1):
            if nums[i+1]<=nums[i]:
                sb=nums[i]-nums[i+1]+1
                nums[i+1]+=sb
                ct+=sb
        return ct
