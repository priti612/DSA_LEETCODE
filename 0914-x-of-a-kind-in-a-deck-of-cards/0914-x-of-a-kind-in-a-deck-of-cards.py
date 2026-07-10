class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        ct=Counter(deck).values()
        g=0
        for gd in ct:
            g=math.gcd(g,gd)
        return g>=2