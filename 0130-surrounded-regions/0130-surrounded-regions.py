class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(r,c):
            if r<0 or c<0 or r>=n or c>=m or board[r][c]!='O':
                return
            board[r][c]='Y'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
                
        n=len(board)
        m=len(board[0])
        for i in range(m):
            if board[0][i]=='O':
                dfs(0,i)
            if board[n-1][i]=='O':
                dfs(n-1,i)
        for r in range(n):
            if board[r][0]=='O':
                dfs(r,0)
            if board[r][m-1]=='O':
                dfs(r,m-1)
        for r in range(n):
            for c in range(m):
                if board[r][c]=='O':
                    board[r][c]='X'
                elif board[r][c]=='Y':
                    board[r][c]='O'
