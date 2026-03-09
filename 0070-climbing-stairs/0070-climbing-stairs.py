class Solution:
    def climbStairs(self, n: int) -> int:
        # if n<=1:
        #     return 1
        # return self.climbStairs(n-1)+self.climbStairs(n-2)
        def sol(n):
            if r[n]!=-1:
                return r[n]
            r[n]=sol(n-1)+sol(n-2)
            return r[n]

        r=[-1]*(n+1)
        r[0]=1
        r[1]=1
        return sol(n)
        