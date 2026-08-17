public class Solution {
    public void ReverseString(char[] s) {
        int left=0;
        int right=s.Length-1;
        while(left<right){
            char ch=s[left];
            s[left]=s[right];
            s[right]=ch;
            left++;
            right--;
        }
    }
}