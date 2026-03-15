class Solution:
    def isNumber(self, s: str) -> bool:
        s=s.strip()
        d=False
        dot=False
        exp=False

        for i ,c in enumerate(s):
            if c.isdigit():
                d=True
            elif c in ['+','-']:
                if i!=0 and s[i-1] not in ['e','E']:
                    return False
            elif c=='.':
                if dot or exp:
                    return False
                dot= True
            elif c in ['e','E']:
                if exp or not d:
                    return False
                exp=True
                d=False
            else:
                return False
        return d
