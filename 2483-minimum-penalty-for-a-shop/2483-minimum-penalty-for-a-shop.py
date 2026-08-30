class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n=len(customers)
        suff=[0]*(n+1)
        for i in range(n):
            suff[i+1]=suff[i]+(1 if customers[i]=='N' else 0)
        nfor=0
        mini=float('inf')
        b=0
        for i in range(n,-1,-1):
            p=suff[i]+nfor
            if(p<=mini):
                mini=p
                b=i
            if i>0 and customers[i-1]=='Y':
                nfor+=1
        return b
        