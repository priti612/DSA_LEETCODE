class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        ct=0
        maxi=0
        f={}
        maxf=0
        while r<len(s):
            f[s[r]]=f.get(s[r],0)+1
            maxf=max(maxf,f[s[r]])
            
            while (r-l+1)-maxf>k:
                f[s[l]]-=1
                l+=1
            maxi=max(maxi,r-l+1)
            r+=1
        return maxi