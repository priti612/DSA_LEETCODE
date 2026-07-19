class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def sol(idx,subset):
            xr=0
            nonlocal sm
            for x in subset:
                xr^=x
            sm+=xr
            for i in range(idx,len(nums)):
                subset.append(nums[i])
                sol(i+1,subset)
                subset.pop()

                


        sm=0
        sol(0,[])
        return sm