class Solution:
    def trap(self, height: List[int]) -> int:
        lmax=0
        rmax=0
        tot=0
        l=0
        r=len(height)-1
        while l<r:
            if height[l]<=height[r]:
                if height[l]>=lmax:
                    lmax=height[l]
                else:
                    tot+=lmax-height[l]
                l+=1
            else:
                if height[r]>=rmax:
                   rmax=height[r]
                else:
                    tot+=rmax-height[r]
                r-=1
        return tot