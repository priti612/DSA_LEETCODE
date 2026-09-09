class Solution:
    def countCommas(self, n: int) -> int:
        ct=0
        tot=1000
        while n>=tot:
            ct+=(n-tot+1)
            tot*=1000
        return ct