public class Solution {
    public string MergeAlternately(string word1, string word2) {
        StringBuilder s=new StringBuilder();
        int i=0;
        int j=0;
        while(i<word1.Length || j<word2.Length){
            if(i<word1.Length){
                s.Append(word1[i]);
                 i++;
            }
            if(j<word2.Length){
            s.Append(word2[j]);
           
            j++;
            }
        }
        return s.ToString();
    }
}