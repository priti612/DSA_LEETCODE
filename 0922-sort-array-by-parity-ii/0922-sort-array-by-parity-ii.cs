public class Solution {
    public int[] SortArrayByParityII(int[] nums) {
        int left=0;
        int right=1;
        int n=nums.Length;
        int[] ans=new int[n];
        while(left<n && right<n){
            if(left%2==0 && nums[left]%2==0){
                // ans.Add(nums[left]);
                left+=2;
            }
            else if(nums[right]%2!=0){
                // ans.Add(nums[right]);
                right+=2;
            }
            else{
                int temp=nums[left];
                nums[left]=nums[right];
                nums[right]=temp;
                left+=2;
                right+=2;
            }
        }
        // return int []ans;
        return nums;
    }
}