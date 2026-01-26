class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        mini=0
        summ=0
        n=len(nums)
        nums.sort()
        for i in range(0,n,2):
            mini=nums[i]
            summ+=nums[i]
        return summ
