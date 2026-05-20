class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        """
        i=0
        j=0
        h=len(nums)-1
        while j<=h:
            if nums[j]==0:
                nums[j],nums[i]=nums[i],nums[j]
                j+=1
                i+=1
            elif nums[j]==1:
                j+=1
            else:
                nums[j],nums[h]=nums[h],nums[j]
                h-=1