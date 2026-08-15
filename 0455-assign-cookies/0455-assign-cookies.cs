public class Solution {
    public int FindContentChildren(int[] g, int[] s) {
        Array.Sort(g);
        Array.Sort(s);
        int ct_g=0;
        int ct_s=0;
        while(ct_g<g.Length && ct_s<s.Length){
            if(s[ct_s]>=g[ct_g]){
                ct_g++;
            }
            ct_s++; 
        }
        return ct_g;
        
    }
}