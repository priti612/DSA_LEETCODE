class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x=0
        for i in nums:
            x^=i
        m=x & -x
        a,b=0,0
        for i in nums:
            if i & m:
                a^=i
            else:
                b^=i
        return [a,b]
            