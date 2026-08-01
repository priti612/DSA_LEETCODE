public class Solution {
    public IList<IList<int>> Subsets(int[] nums) {
        var res=new List<IList<int>>();
        var curr=new List<int>();
        void solve(int idx){
            if (idx==nums.Length){
                res.Add(new List<int>(curr));
                return;
            }
            curr.Add(nums[idx]);
            solve(idx+1);
            curr.RemoveAt(curr.Count-1);

            solve(idx+1);
        }
        solve(0);
        return res;
    }
}