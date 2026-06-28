class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans=[]
        nums.sort()
        n=len(nums)
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=n-1
            while l<r:
                sm=nums[i]+nums[l]+nums[r]
                if sm==0:
                    ans.append([nums[i],nums[l],nums[r]])
                    left=nums[l]
                    right=nums[r]
                    while l<r and left==nums[l]:
                        l+=1
                    while l<r and right==nums[r]:
                        r-=1
                elif sm<0:
                    l+=1
                else:
                    r-=1
        return ans