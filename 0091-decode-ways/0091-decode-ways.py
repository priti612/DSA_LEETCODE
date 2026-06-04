class Solution:
    def numDecodings(self, s: str) -> int:
 
        n=len(s)
        t=[0]*(n+1)
        t[0]=1
        t[1]=1 if s[0]!='0' else 0
        for i in range(2,n+1):
            if s[i-1]!="0":
                t[i]+=t[i-1]
            if s[i-2]=="1" or (s[i-2]=="2" and s[i-1]<="6"):
                t[i]+=t[i-2]
        return t[-1]

