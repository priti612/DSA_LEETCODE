class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp=[[float('inf')] * len(triangle[r]) for r in range(len(triangle))]
        inf=float('inf')
        # for i in range(len(triangle)):
        #     for j in range(len(triangle[i])):
        #         triangle[i][j]=inf
        def dfs(r,c):
            if r>=len(triangle):
                return 0
            if dp[r][c]!=inf:
                return dp[r][c]
            dp[r][c]=triangle[r][c]+min(dfs(r+1,c),dfs(r+1,c+1))
            return dp[r][c]
        return dfs(0,0)