public class Solution {
    public int MaxScore(string s) {
        int n=s.Length;
        int maxi=0;
        for(int i=1;i<n;i++){
            int left=0;
            int right=0;
            for(int j=0;j<i;j++){
                if(s[j]=='0') left++;
            }
            for(int j=i;j<n;j++){
                if(s[j]=='1') right++;

            }
             maxi=Math.Max(maxi,left+right);
        }
        return maxi;
    }
}