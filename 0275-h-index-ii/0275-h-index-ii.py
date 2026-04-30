class Solution:
    def hIndex(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        n=len(nums)
        ans=0
        while low<=high:
            mid=low+(high-low)//2
            print(mid)
            if nums[mid]>=n-mid:
                ans=n-mid
                high=mid-1
            else:
                low=mid+1
        return ans

        
            