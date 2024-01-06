class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> answers = new ArrayList<>();
        int sum;
        Arrays.sort(nums);
        
        for(int i=0; i<nums.length-2; i++){
            if(i>0 && nums[i] == nums[i-1]) continue;
            int left = i + 1;
            int right = nums.length - 1;
            
            while(left < right){
                sum = nums[i] + nums[left] + nums[right];
                
                if(sum > 0){
                    right -= 1;
                }
                else if(sum < 0){
                    left += 1;
                } 
                else {
                    
                    answers.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    
                    while(left < right && nums[left] == nums[left+1])
                        left += 1;
                    while(left < right && nums[right] == nums[right-1])
                        right -= 1;
                    
                    left += 1;
                    right -= 1;
                }
        
            }
                
        }
        return answers;
    }
}