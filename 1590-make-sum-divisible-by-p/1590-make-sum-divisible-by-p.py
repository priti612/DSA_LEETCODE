class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        
        # ct=0
        # if sm%p==0:
        #     return 0
        # for i in range(1,len(nums)):
        #     curr=0
        #     for j in range(len(nums)):
        #         curr+=nums[j]
        #         if j>=i:
        #             curr-=nums[j-i]
        #         if j>=i-1:
        #             rem=sm-curr
        #             if rem%p==0:
        #                 return i
        # return -1

        sm=sum(nums)
        tg=sm%p
        f={0:-1}
        curr=0
        ct=0
        if tg==0:
            return 0
        ans=len(nums)
        for i in range(len(nums)):
            curr+=nums[i]
            rem=curr%p
            need=(rem-tg)%p
            if need in f:
                ans=min(i-f[need],ans)
            f[rem]=i
        return ans if ans<len(nums) else -1
