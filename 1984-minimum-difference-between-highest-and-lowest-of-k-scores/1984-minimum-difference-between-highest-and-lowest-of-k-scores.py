class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if len(nums)==1 and k==1:
            return 0
        n=len(nums)
        maxi=float('inf')
        nums.sort()
        i=0
        j=i+k-1
        while j<n:
            maxi=min(maxi,nums[j]-nums[i])
            i+=1
            j+=1
        return maxi




