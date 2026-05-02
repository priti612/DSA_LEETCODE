class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ct=0
        m=len(flowerbed)
        if m==1 and flowerbed[0]==0:
            return True
        elif m==1 and n==1 and flowerbed[0]==1:
            return False

        if m==1 or n==0:
            return True
        
        
        for i in range(len(flowerbed)-1):
            
            if flowerbed[i]==0 and flowerbed[i-1]!=1 and flowerbed[i+1]!=1:
                flowerbed[i]=1
                ct+=1
                print(ct)
            elif flowerbed[0]==0 and flowerbed[1]==0:
                flowerbed[0]=1
                ct+=1
            elif flowerbed[m-1]==0 and flowerbed[m-2]==0:
                flowerbed[m-1]=1
                ct+=1
            if ct==n:
                return True
        return False
        
