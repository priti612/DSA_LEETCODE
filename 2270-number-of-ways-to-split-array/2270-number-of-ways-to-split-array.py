class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        s2=sum(nums[1:])
        ct=0
        s1=nums[0]
        if s1>=s2:
                ct+=1
        for j in range(1,len(nums)-1):
            s1+=nums[j]
            s2-=nums[j]
            if s1>=s2:
                ct+=1
            
        return ct
