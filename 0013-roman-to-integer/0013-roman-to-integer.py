class Solution:
    def romanToInt(self, s: str) -> int:
        def romo(c):
            if c=="I":
                return 1
            elif c=="V":
                return 5
            elif c=="X":
                return 10
            elif c=="L":
                return 50
            elif c=="C":
                return 100
            elif c=="D":
                return 500
            elif c=="M":
                return 1000
        i=0
        tot=0
        while(i<len(s)-1):
            if romo(s[i])<romo(s[i+1]):
                tot -= romo(s[i])
            else:
                tot += romo(s[i])
            i+=1
        tot+=romo(s[-1])
        return tot
        