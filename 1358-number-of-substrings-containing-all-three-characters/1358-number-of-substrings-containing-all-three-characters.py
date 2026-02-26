class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last={'a':-1,'b':-1,'c':-1}
        ct=0
        for i in range(len(s)):
            last[s[i]]=i
            if last['a']!=-1 and last['b']!=-1 and last['c']!=-1:
                ct+=1+min(last['a'],last['b'],last['c'])
        return ct