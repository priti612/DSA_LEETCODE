class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n=len(stones)
        s=sum(stones)
        s1=s//2
        t=[[False]*(s1+1) for _ in range(n+1)]
    
        for i in range(n+1):
            t[i][0]=True
        for i in range(1,n+1):
            for j in range(1,s1+1):
                if stones[i-1]<=j:
                    t[i][j]=t[i-1][j] or t[i-1][j-stones[i-1]]
                else:
                    t[i][j]=t[i-1][j]
        print(t)
        # ab check krna hau sk s1 hai ya nh
        best=0
        for i in range(s1,-1,-1):
            if t[n][i]:
                best=i
                break
        return s-2*best

