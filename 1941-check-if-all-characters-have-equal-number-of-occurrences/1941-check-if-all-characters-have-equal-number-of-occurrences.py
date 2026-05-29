class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        tg=d[s[0]]
        for i in d:
            if d[i]!=tg:
                return False
        return True