class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue 
            l=i+1
            r=len(nums)-1
            while l<r:
                sm=nums[i]+nums[l]+nums[r]
                if sm==0:
                    
                    ans.append((nums[i],nums[l],nums[r]))
                    
                    left=nums[l]
                    right=nums[r]
                    while l<=r and left==nums[l]:
                        
                        l+=1
                    while l<=r and right==nums[r]:
                        
                        r-=1
                elif sm<0:
                    l+=1
                else:
                    r-=1
        return ans