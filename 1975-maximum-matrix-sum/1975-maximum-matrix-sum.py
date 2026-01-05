class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        summ=0
        mini=float('inf')
        ct=0
        for i in range(n):
            for j in range(m):
                summ+=abs(matrix[i][j])
                mini=min(mini,abs(matrix[i][j]))
                if(matrix[i][j]<0):
                    ct+=1
        if ct%2==0:
            return summ
        return summ-2*mini
