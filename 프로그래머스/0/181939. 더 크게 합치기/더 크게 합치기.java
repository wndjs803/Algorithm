class Solution {
    public int solution(int a, int b) {
        int num1 = Integer.parseInt(Integer.toString(a) + Integer.toString(b));
        int num2 = Integer.parseInt(Integer.toString(b) + Integer.toString(a));
        
        if (num1 > num2) return num1;
        return num2;
    }
}