class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vol='aeiou'
        ct=0
        
        for i in range(k):
            if s[i] in vol:
                ct+=1
        mx=ct
        for i in range(k,len(s)):
            if s[i] in vol:
                ct+=1
            if s[i-k] in vol:
                ct-=1
            mx=max(mx,ct)
        return mx



        # for i in range(len(s)-k+1):
        #     v=s[i:i+k]
        #     ct=0
        #     for ch in v:
        #         if ch in vol:
        #             ct+=1
        #     mx=max(mx,ct)
        # return mx

                