class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        ct=0
        mx=1
        for i in range(0,len(nums)):
            curr=1
            for j in range(i,len(nums)):
                curr*=nums[j]
                if curr<k:
                    ct+=1
                else:
                    break
        return ct