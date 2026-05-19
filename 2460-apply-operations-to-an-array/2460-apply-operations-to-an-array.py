class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for j in range(len(nums)-1):
            if nums[j]==nums[j+1]:
                nums[j]*=2
                nums[j+1]=0
                
        i=0
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1    
        return nums
            
        