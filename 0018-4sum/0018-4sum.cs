public class Solution {
    public IList<IList<int>> FourSum(int[] nums, int target) {
        Array.Sort(nums);
        IList<IList<int>>ans=new List<IList<int>>();
        for(int i=0;i<nums.Length-3;i++){
            if (i>0 && nums[i-1]==nums[i]) continue;
            for(int j=i+1;j<nums.Length-2;j++){
                if ( j>i+1 && nums[j-1]==nums[j]) continue;
                int left=j+1;

                int right=nums.Length-1;
                while(left<right){
                    long sm=(long)nums[i]+nums[j]+nums[left]+nums[right];
                    if(sm==target){
                        ans.Add(new List<int>{ nums[i],nums[j],nums[left],nums[right]});
                        while(left<right && nums[left]==nums[left+1])left++;
                        while(left<right && nums[right]==nums[right-1]) right--;
                        left++;
                        right--;

                    }
                    else if(sm<target){
                        left++;
                    }
                    else{
                        right--;
                    }
                }
            }
        }
        return ans;
    }
}