class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def subarr(nums,k):
            l=r=ct=0
            f={}
            while r<len(nums):
                f[nums[r]]=f.get(nums[r],0)+1
                while len(f)>k:
                    f[nums[l]] -= 1
                    # del f[nums[l]]
                    if f[nums[l]]==0:
                        del f[nums[l]]
                    l+=1
                ct+=(r-l+1)
                r+=1
            return ct
        return subarr(nums,k)-subarr(nums,k-1)
