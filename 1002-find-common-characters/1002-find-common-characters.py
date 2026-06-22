class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        com=Counter(words[0])
        for w in words[1:]:
            com &=Counter(w)
        return list(com.elements())