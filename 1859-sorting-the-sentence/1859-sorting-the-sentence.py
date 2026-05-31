class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split(' ')
        # nm=int(s)
        s.sort(key=lambda x:x[-1])
        
        return " ".join(w[:-1] for w in s)