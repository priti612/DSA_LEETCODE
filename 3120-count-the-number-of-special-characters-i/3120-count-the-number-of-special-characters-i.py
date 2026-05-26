class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ct=0
        s1=set()
        s2=set()

        for i in word:
            if i.islower():
                s1.add(i)
            else:
                s2.add(i)
        for i in s1:
            if i.upper() in s2:
                
                ct+=1
        return ct