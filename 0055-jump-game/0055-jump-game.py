class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxi=0
        for i,nm in enumerate(nums):
            if i>maxi:
                return False
            maxi=max(maxi,i+nums[i])
        return True
