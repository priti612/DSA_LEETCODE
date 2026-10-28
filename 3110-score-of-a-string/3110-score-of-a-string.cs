public class Solution {
    public int ScoreOfString(string s) {
        int sm=0;
        for(int i=0;i<s.Length-1;i++){
            sm+=Math.Abs(s[i]-s[i+1]);
        }
        return sm;
        
    }
}