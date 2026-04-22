class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=float('inf')
        for i in range(len(nums)-1):
            l=i+1
            r=len(nums)-1
            while l<r:
                sm=nums[i]+nums[l]+nums[r]
                if sm==target:
                    return sm
                elif abs(res-target)>abs(sm-target):
                    res=sm
                elif sm<target:
                    l+=1
                else:
                    r-=1
        return res