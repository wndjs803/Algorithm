class Solution {
    public int solution(int[] num_list) {
        String odd = "";
        String even = "";
        
        for (int i = 0; i < num_list.length; i++) {
            int num = num_list[i];
            
            if (num % 2 == 1) {
                odd += Integer.toString(num);
            }
            else {
                even += Integer.toString(num);
            }
        }
        
        return Integer.parseInt(odd) + Integer.parseInt(even);
    }
}