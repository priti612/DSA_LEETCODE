class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        # ct=0
        # mx=1
        # for i in range(0,len(nums)):
        #     curr=1
        #     for j in range(i,len(nums)):
        #         curr*=nums[j]
        #         if curr<k:
        #             ct+=1
        #         else:
        #             break
        # return ct
        ct=0
        left=0
        curr=1
        if k<=0:
            return 0
        for right in range(len(nums)):
            curr*=nums[right]
            while curr>=k:
                curr//=nums[left]
                left+=1

            ct+=(right-left+1)
        return ct