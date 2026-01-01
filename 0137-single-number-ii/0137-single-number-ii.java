class Solution {
    public int singleNumber(int[] nums) {
        int res=0;
        for(int i=0;i<32;i++){
            int ct=0;
            for(int num:nums){
                if((num & (1<<i))!=0){
                ct++;
                }}

            if(ct%3!=0){
            res |= (1<<i);
        }
        }
        return res;
    }
}