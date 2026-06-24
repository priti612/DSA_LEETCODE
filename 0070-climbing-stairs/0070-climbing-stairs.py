class Solution:
    def climbStairs(self, n: int) -> int:
        def sol(n):
            # if n==2:
            #     return 2
            # if n==1:
            #     return 1
            t=[1]*(n+1)
            # t[1]=1
            # t[2]=2
            for i in range(2,n+1):
                t[i]=t[i-1]+t[i-2]
            return t[n]
        return sol(n)