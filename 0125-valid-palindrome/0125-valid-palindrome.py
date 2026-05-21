class Solution:
    def isPalindrome(self, s: str) -> bool:
        w="".join(i.lower() for i in s if i.isalnum())
        left=0
        right=len(w)-1
        while left<right:
            if w[left]!=w[right]:
                return False
            left+=1
            right-=1
        return True