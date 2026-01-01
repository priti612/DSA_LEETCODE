class Solution {
public:
    string addBinary(string a, string b) {
        string str="";
        int i=a.size()-1,j=b.size()-1;
        int ct=0;
        while(i>=0 || j>=0 || ct){
            int sum=ct;
            if(i>=0) sum+=a[i--]-'0';
            if(j>=0) sum+=b[j--]-'0';
            str+=(sum%2)+'0';
            ct=sum/2;

        }
        reverse(str.begin(),str.end());
        return str;
        
    }
};