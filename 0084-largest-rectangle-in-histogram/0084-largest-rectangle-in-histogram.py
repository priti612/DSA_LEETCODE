class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st=[]
        maxi=0
        n=len(heights)
        for i in range(n+1):
            while st and (i==n or heights[st[-1]]>=heights[i]):
                h=heights[st.pop()]
                if not st:
                    w=i
                else:
                    w=i-st[-1]-1
                maxi=max(maxi,w*h)
            st.append(i)
        return maxi