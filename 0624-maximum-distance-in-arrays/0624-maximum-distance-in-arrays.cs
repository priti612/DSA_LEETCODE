public class Solution {
    public int MaxDistance(IList<IList<int>> arrays) {
        int md=0;
        int maxi=arrays[0][arrays[0].Count-1];
        int minso=arrays[0][0];
        for(int i=1;i<arrays.Count;i++){
            int currmin=arrays[i][0];
            int currmax=arrays[i][arrays[i].Count-1];
            md=Math.Max(md,Math.Abs(currmax-minso));
            md=Math.Max(md,Math.Abs(maxi-currmin));
            minso=Math.Min(minso,currmin);
            maxi=Math.Max(maxi,currmax);            
        }
        return md;
    }
}