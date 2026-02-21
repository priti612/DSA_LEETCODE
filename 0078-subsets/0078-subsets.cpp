class Solution {
    void sub(vector<int>& nums,int i,int n,vector<int>temp,vector<vector<int> >&ans){
        if(i==n){
            ans.push_back(temp);
            return;
        }
        sub(nums,i+1,n,temp,ans);
        temp.push_back(nums[i]);
        sub(nums,i+1,n,temp,ans);

    }
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>>ans;
        vector<int>temp;
         sub(nums,0,nums.size(),temp,ans);
         return ans;
    }
};