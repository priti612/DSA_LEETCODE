class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res=[]
        i=0
        for j in spaces:
            res.append(s[i:j])
            i=j
        res.append(s[i:])
        return ' '.join(res)
        