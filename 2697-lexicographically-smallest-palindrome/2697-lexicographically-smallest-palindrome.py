class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left=0
        right=len(s)-1
        ss=list(s)
        while left<right:
            if ss[left]!=ss[right]:
                d=min(ss[left],s[right])
                ss[left]=d
                ss[right]=d
            left+=1
            right-=1
        return "".join(ss)
