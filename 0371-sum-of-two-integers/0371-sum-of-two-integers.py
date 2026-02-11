class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask= 0xFFFFFFFF
        while (b&mask)!=0:
            sm=a^b
            c=(a&b)<<1
            a=sm
            b=c
        return a & mask if b>0 else a