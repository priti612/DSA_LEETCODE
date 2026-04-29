class Solution:
    def bestClosingTime(self, s: str) -> int:
        sc=0
        maxi=0
        best=0

        for i,char in enumerate(s):
            if char=='Y':
                sc+=1
                
            else:
                sc-=1
            if sc>maxi:
                maxi=sc
                best=i+1
        return best