class Solution:
    def nextGreaterElement(self, n: int) -> int:
        d=list(str(n))
        i=len(d)-2
        while i>=0 and d[i]>=d[i+1]:
            i-=1
        if i==-1:
            return -1
        j=len(d)-1
        while d[j]<=d[i]:
            j-=1
        d[i],d[j]=d[j],d[i]
        d[i+1:]=reversed(d[i+1:])
        r=int("".join(d))
        return r if r<2**31 else -1
        