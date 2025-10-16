class Solution {
    public int solution(String num_str) {
        int sum = 0;
        
        for (String s : num_str.split("")) {
            sum += Integer.parseInt(s);
        }
        
        return sum;
    }
}