public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        
        HashSet<int>h=new HashSet<int>();
        foreach(int n in nums){
            if(h.Contains(n)){
               
                return true;
            }
             h.Add(n);
        }
        return false;
    }
}