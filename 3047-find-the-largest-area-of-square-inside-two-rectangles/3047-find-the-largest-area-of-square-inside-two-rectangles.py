class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n=len(bottomLeft)
        maxi=0
        for i in range(n):
            for j  in range(i+1,n):
                left=max(bottomLeft[i][0],bottomLeft[j][0])
                right=min(topRight[i][0],topRight[j][0])
                top=min(topRight[i][1],topRight[j][1])
                bottom=max(bottomLeft[i][1],bottomLeft[j][1])
                if left<right and top>bottom:
                    h=top-bottom
                    w=right-left
                    s=min(h,w)
                    maxi=max(maxi,s*s)
        return maxi

        