public class Solution {
    public int[] RearrangeArray(int[] nums) {
        int[] ans=new int[nums.Length];
        List<int>pos=new List<int>();
        List<int>neg=new List<int>();
        for(int i=0;i<nums.Length;i++){
            if(nums[i]>0){
                pos.Add(nums[i]);

            }
            else if(nums[i]<0){
                neg.Add(nums[i]);
            }
        }
        for(int i=0;i<pos.Count;i++){
            ans[2*i]=pos[i];
            ans[2*i+1]=neg[i];
        }
        return ans;
    }
}