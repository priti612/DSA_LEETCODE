class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        maxi=0
        hlen=256
        hash=[-1]*hlen
        # for i in range(len(s)):
        #     hash[i]-1
        while r<len(s):
            if hash[ord(s[r])]!=-1:
                l=max(hash[ord(s[r])]+1,l)
            ln=r-l+1
            maxi=max(ln,maxi)
            hash[ord(s[r])]=r
            r+=1
        return maxi
