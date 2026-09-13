public class Solution {
    public double FindMedianSortedArrays(int[] nums1, int[] nums2) {
        List<int>ans=new List<int>();
        foreach(int x in nums1)ans.Add(x);
        foreach(int x in nums2) ans.Add(x);
        ans.Sort();
        int n=ans.Count;
        if(n%2==1){
            return (double)ans[n/2];
        }
        else{
            return (ans[n/2-1]+ans[n/2])/2.0;
        }
    }
}