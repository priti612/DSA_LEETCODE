class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        sub=[[]]
        for num in nums:
            sub+=[curr+[num] for curr in sub]
        print(sub)
        sm=0
        for s in sub:
            curr=0
            for i in s:
                curr^=i
            sm+=curr
        return sm