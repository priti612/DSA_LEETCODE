class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        n=len(matrix[0])
        ht=[0]*n
        left=[0]*n
        right=[n]*n
        maxi=0
        for i in range(len(matrix)):
            currleft,currright=0,n
            for j in range(n):
                if matrix[i][j]=="1":
                    ht[j]+=1
                else:
                    ht[j]=0
            print(ht)
            for j in range(n):
                if matrix[i][j]=='1':
                    left[j]=max(left[j],currleft)
                else:
                    left[j]=0
                    currleft=j+1
            # print(left)
            for j in range(n-1,-1,-1):
                if matrix[i][j]=='1':
                    right[j]=min(right[j],currright)
                else:
                    right[j]=n
                    currright=j
            for j in range(n):
                width=right[j]-left[j]
                side=min(ht[j],width)
                maxi=max(maxi,side)
        return maxi*maxi