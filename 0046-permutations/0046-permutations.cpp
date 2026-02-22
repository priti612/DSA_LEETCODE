class Solution {
    public:
    void permute(vector<int>& nums,vector<vector<int>>&ans,vector<int>&temp,vector<int>&vis){
        if(nums.size()==temp.size()){
            ans.push_back(temp);
            return;
        }
        for(int i=0;i<nums.size();i++){
            if(vis[i]==0){
                vis[i]=1;
                temp.push_back(nums[i]);
                permute(nums,ans,temp,vis);
                
                temp.pop_back();
                vis[i]=0;
            }
        }
    }

    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>>ans;
        vector<int>temp;
        vector<int>vis(nums.size(),0);
       
        permute(nums,ans,temp,vis);
        return ans;
    }
};