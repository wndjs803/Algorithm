class Solution {
    public String solution(String code) {
        String answer = "";
        String mode = "0";
        String[] codeSplit = code.split("");

        for (int i = 0; i < codeSplit.length; i++) {
            if (mode.equals("0")) {
                if (!codeSplit[i].equals("1")) {
                    if (i % 2 == 0) answer += codeSplit[i];
                }
                else mode = "1";
            }
            else {
                if (!codeSplit[i].equals("1")) {
                    if (i % 2 == 1) answer += codeSplit[i];
                }
                else mode = "0";
            }
        }
        
        if (answer.equals("")) return "EMPTY";
        return answer;
    }
}