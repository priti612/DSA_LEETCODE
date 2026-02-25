class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        r=0
        maxi=0
        f={}
        while r<len(fruits):
            f[fruits[r]]=f.get(fruits[r],0)+1
            if len(f)>2:
                f[fruits[l]]-=1
                if f[fruits[l]]==0:
                    del f[fruits[l]]
                l+=1
            if len(f)<=2:
                maxi=max(maxi,r-l+1)
            r+=1
        return maxi