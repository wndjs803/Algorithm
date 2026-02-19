class Solution {
    public String solution(String my_string, int[] indices) {
        String[] split = my_string.split("");
        
        for(int index : indices) {
            split[index] = "";
        }
        
        return String.join("", split);
    }
}