class Solution:
    def construct2DArray(self, nums: List[int], m: int, n: int) -> List[List[int]]:
        ans=[]
        if len(nums)!=n*m:
            return []
        for i in range(0,n*m,n):
            ans.append(nums[i:i+n])
        return ans