class Solution {
    public int solution(String my_string, String is_suffix) {
        int start = 0;
        
        while (start < my_string.length()) {
            if (my_string.substring(start, my_string.length()).equals(is_suffix)) return 1;
            start++;
        }
        
        return 0;
    }
}