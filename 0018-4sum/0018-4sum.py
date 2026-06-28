class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        ans=[]
        for i in range(n-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                
                l=j+1
                r=n-1
                while l<r:
                    sm=nums[i]+nums[j]+nums[r]+nums[l]
                    if sm==target:
                        ans.append([nums[i],nums[j],nums[l],nums[r]])
                        left=nums[l]
                        right=nums[r]
                        while l<r and left==nums[l]:
                            l+=1
                        while l<r and right==nums[r]:
                            r-=1
                    elif sm<target:
                        l+=1
                    else:
                        r-=1
        return ans