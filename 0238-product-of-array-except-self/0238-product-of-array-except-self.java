class Solution {
    public int[] productExceptSelf(int[] nums) {
        int length = nums.length;
        int[] array = new int[length];
        
        int p = 1;
        
        for(int i=0; i<length; i++){
            array[i] = p;
            
            p *= nums[i];
        }
        
        p = 1;
        
        for(int i=length-1; i>=0; i--){
            array[i] *= p;
            
            p *= nums[i];
        }
        
        return array;
    }
}