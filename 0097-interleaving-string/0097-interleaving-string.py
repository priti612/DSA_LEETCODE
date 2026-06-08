class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n=len(s1)
        m=len(s2)
        if n+m!=len(s3):
            return False
        # def sol(i,j,k):
        #     if k==len(s3):
        #         return True
        #     if i<n and s1[i]==s3[k]:
        #         if sol(i+1,j,k+1):
        #             return True
        #     if j<m and s2[j]==s3[k]:
        #         if sol(i,j+1,k+1):
        #             return True

        #     return False
        # return sol(0,0,0)
        t=[[False]*(m+1) for _ in range(n+1)]
        t[0][0]=True
        for i in range(n+1):
            for j in range(m+1):
                if i>0:
                    t[i][j]=t[i][j] or (t[i-1][j] and s1[i-1]== s3[i+j-1])
                if j>0:
                    t[i][j]=t[i][j] or (t[i][j-1] and s2[j-1]== s3[i+j-1])
        return t[n][m]
