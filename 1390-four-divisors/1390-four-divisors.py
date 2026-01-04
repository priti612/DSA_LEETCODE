class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        summ=0
        for n in nums:
            div=[]
            for i in range(1,int(math.sqrt(n))+1):
                if n%i==0:
                    div.append(i)
                    if i*i!=n:
                        div.append(n//i)
                if len(div)>4:
                    break
        
            if len(div)==4:
                summ+=sum(div)
        return summ

        