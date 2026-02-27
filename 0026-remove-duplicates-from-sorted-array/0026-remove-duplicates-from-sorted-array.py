class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # i=0
        # for j in range(i,len(nums)):
        #     if nums[i]!=nums[j]:
        #         i+=1
        #     nums[i]=nums[j]
        # return i+1
        u=sorted(set(nums))
        for i in range(len(u)):
            nums[i]=u[i]
        return len(u)
            
                
                
