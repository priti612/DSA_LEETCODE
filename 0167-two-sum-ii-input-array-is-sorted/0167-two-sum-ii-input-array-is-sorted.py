class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        left=0
        n=len(nums)
        right=n-1
        # num=sorted((nm,i) for i,nm in enumerate(nums))
        while left<right:
            sm=nums[left]+nums[right]
            if sm==target:
                return [left+1,right+1]
            elif sm<target:
                left+=1
            else:
                right-=1
        return []

        # mp={}
        # for i,val in enumerate(nums):
        #     sm=target-val
        #     if sm in mp:
        #         return [mp[sm],i]
        #     mp[val]=i
        # return []