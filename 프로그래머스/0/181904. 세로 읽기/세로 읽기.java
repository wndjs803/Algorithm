class Solution {
    public String solution(String my_string, int m, int c) {
        String answer = "";
        
        while (c <= my_string.length()) {
            answer += String.valueOf(my_string.charAt(c - 1));
            c += m;
        }
        return answer;
    }
}