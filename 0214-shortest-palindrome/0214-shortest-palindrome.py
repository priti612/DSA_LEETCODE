class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n=len(s)
        res=s[::-1]
        new=s+'#'+res
        lps=[0]*len(new)
        j=0
        for i in range(1,len(new)):
            while j>0 and new[i]!=new[j]:
                j=lps[j-1]
            if new[i]==new[j]:
                j+=1
            lps[i]=j
        return res[:len(s)-lps[-1]]+s