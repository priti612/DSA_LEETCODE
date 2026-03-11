class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def sol(i,j):
            if j==len(p):
                return i==len(s)
            mt=i<len(s) and (s[i]==p[j] or p[j]=='.')
            if j+1 <len(p) and p[j+1]=='*':
                return sol(i,j+2) or (mt and sol(i+1,j))
            else:
                return mt and sol(i+1,j+1)
        return sol(0,0)