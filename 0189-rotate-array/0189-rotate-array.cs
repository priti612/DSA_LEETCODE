public class Solution {
    public void Rotate(int[] nums, int k) {
        int n=nums.Length;
        k=k%n;
        reversee(nums,0,n-1);
        reversee(nums,0,k-1);
        reversee(nums,k,n-1);
        
    }
    public void reversee(int [] nums,int st,int end){
        while(st<end){
            (nums[st],nums[end])=(nums[end],nums[st]);
            st++;
            end--;
        }
    }
}