class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(c.lower() for c in s if c.isalnum())
        f=0
        l=len(s)-1
        while f<l:
            if s[l]!=s[f]:
                return False
            f+=1
            l-=1
        return True
