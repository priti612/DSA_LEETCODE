class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        n=len(nums)-1
        if len(nums)-1<=0:
            return False

        for i in range(len(nums)-1):
            if nums[i]!=i+1:
                return False
        return nums[-1]==n