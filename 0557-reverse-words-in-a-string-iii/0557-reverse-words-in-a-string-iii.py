class Solution:
    def reverseWords(self, s: str) -> str:
        res=s.split(' ')
        res1=[word[::-1] for word in res]
        return " ".join(res1)