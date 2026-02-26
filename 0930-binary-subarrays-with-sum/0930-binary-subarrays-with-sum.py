class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def gol(goal):
            l=0
            r=0
            sm=0
            ct=0
            while r<len(nums):
                if goal<0:
                    return 0
                sm+=nums[r]
                while sm>goal:
                    sm=sm-nums[l]
                    l+=1
                ct=ct+(r-l+1)
                r+=1
                print(ct)
            return ct
        return gol(goal)-gol(goal-1)