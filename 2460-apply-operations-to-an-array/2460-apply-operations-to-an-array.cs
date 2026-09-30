public class Solution {
    public int[] ApplyOperations(int[] nums) {
        int left=0;
        int right=nums.Length;
        for(int i=0;i<nums.Length-1;i++){
            if(nums[i]==nums[i+1]){
                nums[i]=nums[i]*2;
                nums[i+1]=0;
            }
            
        }
        int zero=0;
        for(int i=0;i<nums.Length;i++){
            if(nums[i]!=0){
                nums[zero]=nums[i];
                zero++;
            }
        }
        while (zero<nums.Length){
            nums[zero]=0;
            zero++;
        }
        return nums;
    }
}