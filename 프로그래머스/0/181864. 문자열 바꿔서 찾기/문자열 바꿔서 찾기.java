class Solution {
    public int solution(String myString, String pat) {
        String answer = "";
        for (String s : myString.split("")) {
            if (s.equals("A")) answer += "B";
            else answer += "A";
        }
        
        if (answer.contains(pat)) return 1;
        return 0;
        
    }
}