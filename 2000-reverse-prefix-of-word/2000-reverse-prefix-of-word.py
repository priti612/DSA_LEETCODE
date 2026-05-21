class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx=word.find(ch)
        if ch not in word:
            return word
        left=0
        word=[i for i in word]
        while left<idx:
            word[left],word[idx]=word[idx],word[left]
            left+=1
            idx-=1
        return "".join(word)
                