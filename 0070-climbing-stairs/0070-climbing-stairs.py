class Solution:
    def climbStairs(self, n: int) -> int:
        
        def sol(n):
            if t[n]!=-1:
                return t[n]
            t[n]=sol(n-1)+sol(n-2)
            return t[n]
        t=[-1]*(n+1)
        t[0]=1
        t[1]=1
        return sol(n)