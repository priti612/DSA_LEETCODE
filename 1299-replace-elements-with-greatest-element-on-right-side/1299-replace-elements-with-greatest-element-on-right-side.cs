public class Solution {
    public int[] ReplaceElements(int[] nums) {
        int n=nums.Length;
        int max=-1;
        for(int i=n-1;i>=0;i--){
            int far=nums[i];
            nums[i]=max;
            max=Math.Max(max,far);
        }
        return nums;
        
    }
}