class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        s=bin(n)
        ct=0
        for i in range(len(s)-1):
            
            if s[i]=="1" and s[i+1]=="1":
                ct+=1
        return ct==1
        # return "11" in bin(n)
