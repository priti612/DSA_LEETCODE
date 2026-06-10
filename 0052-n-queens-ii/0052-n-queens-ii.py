class Solution:
    def totalNQueens(self, n: int) -> int:
        res=[]
        b=[['.']*n for _ in range(n)]
        row,col,pos,neg=set(),set(),set(),set()
        def sol(i):
            if i==n:
                res.append(["".join(p) for p in b])
            for j in range(n):
                if i in row or j in col or i+j in pos or i-j in neg or b[i][j]=='Q':
                    continue
                b[i][j]="Q"
                row.add(i)
                col.add(j)
                pos.add(i+j)
                neg.add(i-j)
                sol(i+1)
                row.discard(i)
                col.discard(j)
                pos.discard(i+j)
                neg.discard(i-j)
                b[i][j]='.'
        sol(0)
        return len(res)