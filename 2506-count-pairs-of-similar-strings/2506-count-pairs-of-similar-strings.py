class Solution:
    def similarPairs(self, words: List[str]) -> int:
        ct=0
        w=[set(word) for word in words]
        for i in range(len(w)):
            for j in range(i+1,len(w)):
                if w[i]==w[j]:
                    ct+=1
        return ct