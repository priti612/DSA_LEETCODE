class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d={}
        res=[]
        for i in range(len(s)-9):
            sub=s[i:i+10]
            if sub not in d:
                d[sub]=1
            else:
                d[sub]+=1
                if d[sub]==2:
                    res.append(sub)
        return res

