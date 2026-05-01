class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m=len(matrix[0])
        low=0
        high=m-1
        while low<n and high>=0:
            # mid=low+(high-low)//2
            if matrix[low][high]==target:
                return True
            elif matrix[low][high]<target:
                low=low+1
            else:
                high-=1
        return False