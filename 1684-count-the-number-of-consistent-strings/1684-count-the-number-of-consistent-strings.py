class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ct=0
        alll=set(allowed)
        for w in words:
                if set(w).issubset(alll):
                    ct+=1

        return ct