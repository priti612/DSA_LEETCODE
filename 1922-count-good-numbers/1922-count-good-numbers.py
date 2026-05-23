class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod=10**9+7
        ev=(n+1)//2
        odd=n//2
        et=pow(5,ev,mod)
        od=pow(4,odd,mod)
        return (et*od)%mod
        