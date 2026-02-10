class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        
        for i in range(n+1):
            num=i
            ct=0
            while num>0:
                if num&1:
                    ct+=1
                num>>=1
            res.append(ct)
        return res
        