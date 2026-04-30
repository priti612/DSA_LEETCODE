class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sz=float('inf')
        n=len(nums)
        left=0
        curr=0
        for right in range(n):
            # sm=0
            # for j in range(i,n):
            #     sm+=nums[j]
            #     if sm>=target:
            #         l=j-i+1
            #         sz=min(sz,l)
            #         # print(sz)
            #         break
            curr+=nums[right]
            while curr>=target:
                sz=min(sz,right-left+1)
                curr-=nums[left]
                left+=1

        return sz if sz!=float('inf') else 0

