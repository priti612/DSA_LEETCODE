public class Solution {
    public int LengthOfLastWord(string s) {
        int ct=0;
        s=s.TrimEnd();
        for(int i=s.Length-1;i>=0;i--){
            // ct+=1;
            if(s[i]==' '){
                return ct;
            }
             ct+=1;
        }
        return ct;
    }
}