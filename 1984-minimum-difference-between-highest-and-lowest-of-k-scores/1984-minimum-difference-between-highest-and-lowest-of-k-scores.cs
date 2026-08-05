public class Solution {
    public int MinimumDifference(int[] nums, int k) {
        int left=0;
        int right=k-1;
        Array.Sort(nums);
        int res=int.MaxValue;
        while(right<nums.Length){
            res=Math.Min(res,Math.Abs(nums[left]-nums[right]));
            left++;
            right++;
        }
        return res;
        
    }
}