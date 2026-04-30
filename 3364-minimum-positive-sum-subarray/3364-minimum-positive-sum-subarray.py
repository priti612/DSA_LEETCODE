class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        mini=float('inf')
        n=len(nums)
        for i in range(n):
            sm=0
            for j in range(i,n):
                sm+=nums[j]
                length=j-i+1
                if l<=length<=r:
                    if sm>0:
                        mini=min(mini,sm)
                elif length>r:
                    break
        return mini if mini!=float('inf') else -1


