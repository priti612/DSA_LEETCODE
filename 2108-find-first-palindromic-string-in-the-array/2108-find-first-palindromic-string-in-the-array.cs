public class Solution {
    public string FirstPalindrome(string[] words) {
        
        
        foreach(string ch in words){
            if(plaind(ch)){
                return ch;
            }


        }
        return "";
    }

        private bool plaind(string s){
            int left=0;
            int right=s.Length-1;
            while(left<right){
                if(s[left]!=s[right]){
                    return false;
                }
                left++;
                right--;
            }
            return true;
        }
    }
