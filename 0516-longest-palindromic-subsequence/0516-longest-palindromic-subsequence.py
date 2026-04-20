class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s1=s[::-1]
        n=len(s)
        m=len(s1)
        t=[[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s1[j-1]==s[i-1]:
                    t[i][j]=1+t[i-1][j-1]
                else:
                    t[i][j]=max(t[i-1][j],t[i][j-1])
        return t[n][m]