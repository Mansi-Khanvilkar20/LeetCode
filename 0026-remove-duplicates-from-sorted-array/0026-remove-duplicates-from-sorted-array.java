class Solution {
    public int removeDuplicates(int[] nums) {
             int ind=0, i=1;
        for(i=1;i<nums.length;i++){
            if(nums[i] != nums[i-1]){
                nums[ind]=nums[i-1];
                ind++;
            }
        }
        nums[ind]=nums[nums.length-1];
        return ind+1;
        
    }
}