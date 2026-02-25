class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        maxi=0
        zero=0
        while r<len(nums):
            if nums[r]==0:
                zero+=1
            if zero>k:
                if nums[l]==0:
                    zero-=1
                l+=1
            if zero<=k:
                ln=r-l+1
                maxi=max(ln,maxi)
            r+=1
        return maxi
            