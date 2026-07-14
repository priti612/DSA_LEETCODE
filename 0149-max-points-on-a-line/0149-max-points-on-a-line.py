class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        if n<=2:
            return n
        maxi=1
        for i in range(n):
            f=defaultdict(int)
            for j in range(i+1,n):
                dy=points[j][1]-points[i][1]
                dx=points[j][0]-points[i][0]

                d=math.gcd(dy,dx)
                x,y=dy//d,dx//d
                if x<0 or (x==0 and y<0):
                    x,y=-x,-y
                red=(x,y)
                f[red]+=1
                maxi=max(maxi,f[red]+1)
        return maxi
