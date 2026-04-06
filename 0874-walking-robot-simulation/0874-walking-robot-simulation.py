class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx=[0,1,0,-1]
        dy=[1,0,-1,0]
        d=0
        x,y=0,0
        ob=set(map(tuple,obstacles))
        maxi=0
        for cd in commands:
            if cd==-1:
                d=(d+1)%4
            elif cd==-2:
                d=(d+3)%4
            else:
                for _ in range(cd):
                    nx=x+dx[d]
                    ny=y+dy[d]

                    if (nx,ny) in ob:
                        break
                    x,y=nx,ny
                    maxi=max(maxi,x*x+y*y)
        return maxi