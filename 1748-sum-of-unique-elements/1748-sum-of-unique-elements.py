class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        sm=0
        for i in d:
            if d[i]<2:
                sm+=i
        return sm