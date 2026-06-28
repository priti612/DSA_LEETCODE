class Solution:
    def maxArea(self, height: List[int]) -> int:
        right=len(height)-1
        left=0
        maxi=0
        while left<=right:
            w=right-left
            a=min(height[right],height[left])*w
            maxi=max(maxi,a)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxi
