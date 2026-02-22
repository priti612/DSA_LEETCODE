class Solution {
public:
void permutaion(vector<int>& nums,vector<vector<int>>&ans,int idx){
    if(idx==nums.size()){
        ans.push_back(nums);
        return;
    }
    vector<bool>use(21,0);
    for(int i=idx;i<nums.size();i++){
        if(use[nums[i]+10]==0){
            swap(nums[i],nums[idx]);
            
            permutaion(nums,ans,idx+1);
            swap(nums[i],nums[idx]);
            use[nums[i]+10]=1;
        }
    }

}
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>>ans;
        permutaion(nums,ans,0);
        return ans;
    }
};