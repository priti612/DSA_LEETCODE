class Solution:
    def firstUniqChar(self, s: str) -> int:
        f={}
        for i in s:
            f[i]=f.get(i,0)+1
        for i in range(len(s)):
            ch=s[i]
            if f[ch]==1:
                return i
        return -1