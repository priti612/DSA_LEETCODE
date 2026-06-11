class Solution:
    def lpsss(self,pat,m,lps):
            l=0
            lps[0]=0
            i=1
            while i<m:
                if pat[i]==pat[l]:
                    l+=1
                    lps[i]=l
                    i+=1
                else:
                    if l!=0:
                        l=lps[l-1]
                        
                    else:
                        lps[i]=0
                        i+=1
    def strStr(self, txt: str, pat: str) -> int:
        
        n=len(txt)
        m=len(pat)
        lps=[0]*m
        if not pat:
            return 0
        self.lpsss(pat,m,lps)
        i,j=0,0
        while i<n:
            if txt[i]==pat[j]:
                i+=1
                j+=1
                if j==m:
                    return i-j
                    j=lps[j-1]
            else:
                if j!=0:
                    j=lps[j-1]
                else:
                    i+=1
        return -1