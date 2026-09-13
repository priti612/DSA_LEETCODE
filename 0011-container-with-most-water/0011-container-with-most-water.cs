public class Solution {
    public int MaxArea(int[] height) {
        int left=0;
        int n=height.Length-1;
        int right=n;
        int maxi=0;
        int ans=0;
        while(left<right){
            int mx=Math.Min(height[left],height[right])*(right-left);
            ans=Math.Max(ans,mx);
            if(height[left]<height[right]){
                left++;
            }
            else{
                right--;
            }

        }
        return ans;
    }
}