class Solution {
    public String solution(String[] my_strings, int[][] parts) {
        String answer = "";
        
        for (int i = 0; i < parts.length; i++) {
            String my_string = my_strings[i];
            int start = parts[i][0];
            int end = parts[i][1];
            
            if(start < end) {
                answer += my_string.substring(start, end + 1);
            }
            else if (start == end) {
                answer += String.valueOf(my_string.charAt(start));
            }
            
        }
        
        return answer;
    }
}