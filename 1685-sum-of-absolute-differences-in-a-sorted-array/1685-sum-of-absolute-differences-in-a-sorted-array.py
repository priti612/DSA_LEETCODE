class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        r=sum(nums)
        l=0
        n=len(nums)
        for i in range(len(nums)):
            org=nums[i]
            r-=org
            nums[i]=(i*org-l)+(r-(n-1-i)*org)
            l+=org
        return nums