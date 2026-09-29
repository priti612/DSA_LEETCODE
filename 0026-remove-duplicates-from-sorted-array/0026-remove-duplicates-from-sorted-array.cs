public class Solution {
    public int RemoveDuplicates(int[] nums) {
        HashSet<int>h=new HashSet<int>();
        int i=0;
        foreach(int n in nums){
            if(h.Add(n)){
                nums[i]=n;
                i++;

            }
        }
        return i;
    }
}