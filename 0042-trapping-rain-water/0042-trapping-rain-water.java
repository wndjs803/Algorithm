class Solution {
    public int trap(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int left_max = height[left];
        int right_max = height[right];
        int sum = 0;
        
        while(left < right){
            if(left_max >= right_max){
                sum += right_max - height[right];
                right -= 1;
            }
            else{
                sum += left_max - height[left];
                left += 1;
            }
            
            left_max = Math.max(left_max, height[left]);
            right_max = Math.max(right_max, height[right]);
        }
        
        return sum;
    }
}