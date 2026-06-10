class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def sol(i,j,idx):
            n=len(board)
            m=len(board[0])
            if idx==len(word):
                return True

            d=[(1,0),(0,1),(-1,0),(0,-1)]

            if i<0 or j<0 or j>=m or i>=n or board[i][j]!=word[idx]:
                return False
            temp=board[i][j]
            board[i][j]="#"
            found=(
            sol(i+1,j,idx+1) or
            sol(i,j-1,idx+1) or
            sol(i-1,j,idx+1) or
            sol(i,j+1,idx+1)
            )
            board[i][j]=temp
            return found
        for r in range(len(board)):
            for c in range(len(board[0])):
                if sol(r,c,0):
                    return True

        
        return False