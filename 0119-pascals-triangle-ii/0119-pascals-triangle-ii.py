class Solution:
    def getRow(self, n: int) -> List[int]:
        
        t=[[1]*(i+1) for i in range(n+1)]
        
        for i in range(2,n+1):
            for j in range(1,i):
                t[i][j]=t[i-1][j-1]+t[i-1][j]
        print(t[n])
        return t[n]
        