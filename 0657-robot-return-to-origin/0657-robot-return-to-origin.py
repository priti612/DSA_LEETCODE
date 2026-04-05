class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ct=Counter(moves)
        if (ct["L"]==ct["R"]) and (ct["U"]==ct["D"]):
            return True
        return False
