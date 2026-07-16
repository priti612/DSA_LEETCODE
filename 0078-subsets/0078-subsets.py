class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def solve(idx,subset):
            if idx==len(nums):
                ans.append(subset.copy())
                return
            subset.append(nums[idx])
            solve(idx+1,subset)
            subset.pop()
            solve(idx+1,subset)
        solve(0,[])
        return ans