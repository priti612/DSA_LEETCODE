public class Solution {
    public int MaxSubArray(int[] nums) {
        int sm=nums[0];
        int maxi=nums[0];
       for(int i=1;i<nums.Length;i++){
        sm=Math.Max(nums[i],nums[i]+sm);
        maxi=Math.Max(sm,maxi);
       }
        return maxi;
    }
}