class Solution:
    def longestPrefix(self, pat: str) -> str:
        l=0
        m=len(pat)
        lps=[0]*m
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
        kmp=lps[-1]
        return pat[:kmp]
    