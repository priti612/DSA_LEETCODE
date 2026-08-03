public class Solution {
    public bool ValidPalindrome(string s) {
        int left=0;
        int right=s.Length-1;
        while(left<right){
            if(s[left]!=s[right]){
                return isplaindrom(s,left+1,right) || isplaindrom(s,left,right-1);
            }
            left++;
            right--;
        }
        return true;
    }
    public bool isplaindrom(string s,int i,int j){
        while(i<j){
            if(s[i]!=s[j]){
                return false;
            }
            i++;
            j--;
        }
        return true;

    }
}