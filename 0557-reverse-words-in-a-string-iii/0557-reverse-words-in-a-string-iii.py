class Solution:
    def reverseWords(self, s: str) -> str:
        s=list(s.split())
        res=[]
        for i in s:
            j=i[::-1]
            res.append(j)
        return " ".join(res)
