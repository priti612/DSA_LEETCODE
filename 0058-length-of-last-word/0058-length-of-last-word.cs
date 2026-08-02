public class Solution {
    public int LengthOfLastWord(string b) {
        int ct=0;
        string s=b.Trim();
        for(int i=s.Length-1;i>=0;i--){
            if(s[i]!=' '){
                ct+=1;
            }
            else if(ct>0){
                break;
            }
        }
        return ct;


    }
}