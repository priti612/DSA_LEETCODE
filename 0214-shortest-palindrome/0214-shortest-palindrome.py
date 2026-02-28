class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        res=""
        if len(s)==1:
            return s
        for i in range(len(s),-1,-1):
            res=s[:i]
            if res==res[::-1]:
                add=s[i:][::-1]
                return add+s
            # print(res)
        return ""

