class Solution {
    public int solution(String number) {
        int num = 0;
        
        for (int i = 0; i < number.length(); i++) {
            char c = number.charAt(i);
            num += c - '0';
        }
        
        return num % 9;
    }
}